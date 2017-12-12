import threading                                         #threading

from oslo_db import exception as db_exc                  #db exception module
from oslo_db.sqlalchemy import enginefacade              #session handing
from oslo_db.sqlalchemy import utils as sqlalchemyutils  #make query easier for session
from oslo_log import log as logging                      #oslo_log log

from oslo_utils import strutils                          #strutils.is_int_like()
from oslo_utils import timeutils                         #time module
from oslo_utils import uuidutils                         #uuid module

from sqlalchemy import or_                               #
from sqlalchemy.orm.exc import NoResultFound             #sqlalchemy_ exception class
from sqlalchemy.orm import joinedload                    #
from sqlalchemy.sql.expression import desc               #
from sqlalchemy.sql import true                          #

from myweb.common import exception                       # common exception
from myweb.common.i18n import _                          #_
#from mogan.db import api                                 #metadata class api
from myweb.db.sqlalchemy_ import models                   #db models


_CONTEXT = threading.local()
#LOG = logging.getLogger(__name__)

'''
def get_backend():
    """The backend is this module itself."""
    return Connection()
'''

def _session_for_read():        #session for read
    return enginefacade.reader.using(_CONTEXT)


def _session_for_write():       #session for write
    return enginefacade.writer.using(_CONTEXT)


def model_query(context, model, *args, **kwargs):   #use for query
    """Query helper for simpler session usage.

    :param context: Context of the query
    :param model: Model to query. Must be a subclass of ModelBase.
    :param args: Arguments to query. If None - model is used.

    Keyword arguments:

    :keyword project_only:
      If set to True, then will do query filter with context's project_id.
      if set to False or absent, then will not do query filter with context's
      project_id.
    :type project_only: bool
    """

    if kwargs.pop("project_only", False):
        kwargs["project_id"] = context.tenant

    with _session_for_read() as session:
        query = sqlalchemyutils.model_query(
            model, session, args, **kwargs)
        return query


def add_identity_filter(query, value):   #check int uuid
    """Adds an identity filter to a query.

    Filters results by ID, if supplied value is a valid integer.
    Otherwise attempts to filter results by UUID.

    :param query: Initial query to add filter to.
    :param value: Value for filtering results by.
    :return: Modified query.
    """
    if strutils.is_int_like(value):
        return query.filter_by(id=value)
    elif uuidutils.is_uuid_like(value):
        return query.filter_by(uuid=value)
    else:
        raise exception.InvalidParameterValue(identity=value)


def _dict_with_extra_specs(flavor_query):
    """Takes a server type query and returns it as a dictionary."""
    flavor_dict = dict(flavor_query)
    extra_specs = {x['key']: x['value']
                   for x in flavor_query['extra_specs']}
    flavor_dict['extra_specs'] = extra_specs
    return flavor_dict

#liu
def _dict_with_aggregate_fields(aggregate_query):
    """Takes a aggregate query and returns it as a dictionary."""
    aggregate_dict = dict(aggregate_query)

    # metadata
    metadata = {x['key']: x['value']
                   for x in aggregate_dict['metadata']}
    aggregate_dict['metadata'] = metadata



    return aggregate_dict


class Connection(object):

    #aggregate  liu
    def aggregate_create(self, context, values):
        if not values.get('uuid'):
            values['uuid'] = uuidutils.generate_uuid()

        if not values.get('availability_zone'):
            values['availability_zone'] = ""

        aggregate = models.Aggregates()
        aggregate.update(values)

        with _session_for_write() as session:
            try:
                session.add(aggregate)
                session.flush()
            except db_exc.DBDuplicateEntry:
                raise exception.AggregateAlreadyExists(uuid=values['uuid'])
            return _dict_with_aggregate_fields(aggregate)

    def aggregate_get(self, context, aggregate_uuid):
        query = model_query(context, models.Aggregates).filter_by(
            uuid=aggregate_uuid)

        try:
            return _dict_with_aggregate_fields(query.one())
        except NoResultFound:
            raise exception.AggregateNotFound(
                uuid=aggregate_uuid)

    def aggregate_get_all(self, context):
        query = model_query(context, models.Aggregates)
        return [_dict_with_aggregate_fields(i) for i in query.all()]

    def aggregate_destroy(self, context, aggregate_uuid):
        with _session_for_write():
            # First clean up all metadata related to this aggregate
            aggregate_id = _get_id_from_aggregate(context, aggregate_uuid)
            metadata_query = model_query(
                context,
                models.AggregateMetadata).filter_by(
                aggregate_uuid=aggregate_id)
            metadata_query.delete()

            # Clean up all host related to this aggregate
            host_query = model_query(
                context,
                models.AggregateHosts).filter_by(
                aggregate_uuid=aggregate_id)
            host_query.delete()

            # Then delete the aggregate record
            query = model_query(context, models.Aggregates)
            query = add_identity_filter(query, aggregate_uuid)

            count = query.delete()
            if count != 1:
                raise exception.AggregateNotFound(
                    uuid=aggregate_uuid)

    def aggregate_update(self, context, aggregate_id, values):
        with _session_for_write():
            query = model_query(context, models.Aggregates)
            query = add_identity_filter(query, aggregate_id)
            try:
                ref = query.with_lockmode('update').one()
            except NoResultFound:
                raise exception.AggregateNotFound(
                    uuid=aggregate_id)

            ref.update(values)
            return ref

    def aggregate_host_get(self, context, aggregate_id):
        return _aggregate_host_query(context, aggregate_id)

    def aggregate_host_add(self, context, aggregate_id, host_id):
        host_ref = models.AggregateHosts()
        host_ref.update({"aggregate_uuid":aggregate_id,
                         "host_id":host_id})
        with _session_for_write() as session:
            try:
                session.add(host_ref)
                session.flush()
            except db_exc.DBDuplicateEntry:
                raise exception.AggregateHostExists(aggregate_id=aggregate_id,
                                                    host_id=host_id)

    def aggregate_host_remove(self, context, aggregate_id, host_id):
        count = _aggregate_host_query(context, aggregate_id). \
            filter(host_id=host_id).\
            delete(synchronize_session=False)

        if count == 0:
            raise exception.AggregateHostNotFound(aggregate_id=aggregate_id,
                                                  host_id=host_id)

    def aggregate_metadata_get(self, context, aggregate_id):
        rows = _aggregate_metadata_get_query(context, aggregate_id).all()
        return {row['key']: row['value'] for row in rows}

    def aggregate_metadata_delete(self, context, aggregate_id, key):
        result = _aggregate_metadata_get_query(context, aggregate_id). \
            filter(models.AggregateMetadata.key == key). \
            delete(synchronize_session=False)
        # did not find the metadata
        if result == 0:
            raise exception.AggregateMetadataNotFound(
                aggregate_id=aggregate_id, metadata=key)

    def metadata_update_or_create(self, context,
                                     aggregate_uuid, metadata,
                                     max_retries=10):
        """Create or update aggregate metadata.

        This adds or modifies the key/value pairs specified in the
        metadata dict argument
        """
        for attempt in range(max_retries):
            with _session_for_write() as session:
                try:
                    metadata_refs = model_query(
                        context, models.AggregateMetadata). \
                        filter_by(aggregate_uuid=aggregate_uuid). \
                        filter(models.AggregateMetadata.key.in_(
                            metadata.keys())).with_lockmode('update').all()

                    existing_keys = set()
                    for metadata_ref in metadata_refs:
                        key = metadata_ref["key"]
                        existing_keys.add(key)
                        metadata_ref.update({"value": metadata[key]})

                    for key, value in metadata.items():
                        if key in existing_keys:
                            continue
                        metadata_ref = models.AggregateMetadata()
                        metadata_ref.update(
                            {"key": key, "value": value,
                             "aggregate_uuid": aggregate_uuid})

                        session.add(metadata_ref)
                        session.flush()

                    return metadata
                except db_exc.DBDuplicateEntry:
                    # a concurrent transaction has been committed,
                    # try again unless this was the last attempt
                    if attempt == max_retries - 1:
                        raise exception.AggregateMetadataUpdateCreateFailed(
                            id=aggregate_uuid, retries=max_retries)


#liu
def _get_id_from_aggregate_query(context, aggregate_id):
    return model_query(context, models.Aggregates). \
        filter_by(uuid=aggregate_id)

def _get_id_from_aggregate(context, aggregate_id):
    result = _get_id_from_aggregate_query(context, aggregate_id).first()
    if not result:
        raise exception.AggregateNotFound(uuid=aggregate_id)
    return result.uuid

def _aggregate_host_query(context, aggregate_id):
    return model_query(context, models.AggregateHosts). \
        filter_by(aggregate_uuid=aggregate_id)

def _aggregate_metadata_get_query(context, aggregate_id):
    return model_query(context, models.AggregateMetadata).\
        filter_by(aggregate_uuid=aggregate_id)

if __name__ == '__main__':
    c = Connection()
    print c.aggregate_get_all(context={})
