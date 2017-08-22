

import pecan
import wsme
from pecan import rest
from wsme import types as wtypes
from six.moves import http_client

from myweb.api.controllers import base
from myweb.api.controllers import link
#from myweb.api.controllers.v1.schemas import aggregate_host
from myweb import objects
#from myweb.objects import aggregate
from myweb.api.controllers.v1 import types
from myweb.api import expose
#from myweb.api import validation
from myweb.common import exception
#from mogan.common import policy
from myweb.common.i18n import _




def _make_dict_host(aggregate):
    vals = []
    for host_id in aggregate['hosts']:
        vals.append(host_id)

    return {'aggregate_hosts':vals}

class HostAggregate(base.APIBase):
    """API representation of host aggregate """

    uuid = types.uuid
    """The UUID of the host aggregate"""

    name = wtypes.text    #wsme.wsattr(wtypes.text, mandatory=True)
    """The name of the host aggregate"""

    availability_zone = wtypes.text
    """The availability zone of the host aggregate"""

    #host = [wtypes.text]
    #"""a host list of the host aggregate"""

    metadata = {wtypes.text:types.jsontype}
    """The metadata of the host aggregate"""

    links = wsme.wsattr([link.Link], readonly=True)
    """A list containing a self link"""

    def __init__(self, **kwargs):
        self.fields = []
        for field in objects.Aggregate.fields:
            # Skip fields we do not expose.
            if not hasattr(self, field):
                continue
            self.fields.append(field)
            setattr(self, field, kwargs.get(field, wtypes.Unset))

    @classmethod
    def convert_with_links(cls, rpc_aggregate):
        aggregate = HostAggregate(**rpc_aggregate.as_dict())
        url = pecan.request.public_url
        aggregate.links = [link.Link.make_link('self', url,
                                            'aggregates',
                                            aggregate.uuid),
                        link.Link.make_link('bookmark', url,
                                            'aggregates',
                                            aggregate.uuid,
                                            bookmark=True)
                        ]

        return aggregate

class HostAggregateCollection(base.APIBase):
    """API representation of a collection of  host aggregate """

    host_aggregates = [HostAggregate]
    """A list containing host aggregate objects"""

    @staticmethod
    def convert_with_links(aggregates, url=None, **kwargs):
        collection = HostAggregateCollection()
        collection.aggregates = [HostAggregate.convert_with_links(aggregate)
                              for aggregate in aggregates]
        return collection



class AggregateHostController(rest.RestController):
    """REST controller for aggregate host"""

    #@policy.authorize_wsgi('mogan:aggregate_host', 'add_aggregate_host')
    @expose.expose(None, types.uuid, body=types.jsontype,
                   status_code=http_client.NO_CONTENT)
    def post(self, aggregate_uuid, host):
        """add aggregate host for given aggregate"""

        #validation.check_schema(host, aggregate_host.add_aggregate_host)
        aggregate = objects.Aggregate.get(pecan.request.context, aggregate_uuid)

        try:
            aggregate.hosts.append(host['host_id'])
            aggregate.save()
        except exception.AggregateNotFound as e:
            raise wsme.exc.ClientSideError(
                e.message, status_code=http_client.NOT_FOUND)
        except exception.AggregateHostExists as err:
            raise wsme.exc.ClientSideError(
                err.message, status_code=http_client.CONFLICT)


    #@policy.authorize_wsgi('mogan:aggregate_host', 'get_all')
    @expose.expose(wtypes.text, types.uuid)
    def get_all(self, aggregate_uuid):
        """Retrieve a list of host for given aggregate"""

        aggregate = objects.Aggregate.get(pecan.request.context,
                                          aggregate_uuid)

        return _make_dict_host(aggregate)


    #@policy.authorize_wsgi('mogan:aggregate_host', 'remove_aggregate_host')
    @expose.expose(None, types.uuid, types.uuid,
                   status_code=http_client.NO_CONTENT)
    def delete(self, aggregate_uuid, host_id):
        """Remove aggregate host for given host"""

        aggregate = objects.Aggregate.get(pecan.request.context,
                                          aggregate_uuid)

        try:
            if host_id in aggregate.hosts:
                aggregate.hosts.remove(host_id)
                aggregate.save()
            else:
                raise exception.AggregateHostNotFound(aggregate_id=aggregate_uuid,
                                                     host_id=host_id)
        except (exception.AggregateHostNotFound,
                exception.AggregateNotFound) as e:
            raise wsme.exc.ClientSideError(
                e.message, status_code=http_client.NOT_FOUND)


class AggregateMetadataController(rest.RestController):
    """REST controller for aggregate metadata"""

    #@policy.authorize_wsgi("mogan:aggregate_metadata", "get_all")
    @expose.expose(wtypes.text, types.uuid)
    def get_all(self, aggregate_uuid):
        """Retrieve a list of metadata of the queried aggregate."""

        aggregate = objects.Aggregate.get(pecan.request.context, aggregate_uuid)
        return dict(metadata=aggregate.metadata)


    #@policy.authorize_wsgi("mogan:aggregate_metadata", "patch")
    @expose.expose(types.jsontype, types.uuid, body=types.jsontype,
                   status_code=http_client.ACCEPTED)
    def patch(self, aggregate_uuid, metadata):
        """Create/update metadata for the given aggregate."""

        aggregate = objects.Aggregate.get(pecan.request.context, aggregate_uuid)
        aggregate.metadata = dict(aggregate.metadata, **metadata)
        aggregate.save()
        return dict(metadata=aggregate.metadata)


    #@policy.authorize_wsgi("mogan:aggregate_metadata", "delete")
    @expose.expose(None, types.uuid, wtypes.text,
                   status_code=http_client.NO_CONTENT)
    def delete(self, aggregate_uuid, metadata_key):
        """Delete an metadata for the given aggregate."""

        aggregate = objects.Aggregate.get(pecan.request.context, aggregate_uuid)
        del aggregate.metadata[metadata_key]
        aggregate.save()


class AggregateController(rest.RestController):
    """REST controller for aggregate"""

    metadata = AggregateMetadataController()
    host = AggregateHostController()


    #@policy.authorize_wsgi('mogan:aggregate', 'get_all')
    @expose.expose(HostAggregateCollection)
    def get_all(self):
        """Retrieve a list of aggregate"""
        print 'I am get all aggregates'
        con = pecan.request.context
        #from myweb.db.api_myweb import Connection
        #print Connection.aggregate_get_all(con)
        #from myweb.objects.aggregate import Aggregate
        #aggregates = Aggregate.list(pecan.request.context)
        #return HostAggregateCollection.convert_with_links(aggregates)


    #@policy.authorize_wsgi('mogan:aggregate', 'get_one')
    @expose.expose(HostAggregate, types.uuid)
    def get_one(self, aggregate_uuid):
        """Retrieve information about the given aggregate.
        :param aggregate_uuid:UUID of an aggregate
        """
        rpc_aggregate = objects.Aggregate.get(pecan.request.context, aggregate_uuid)
        return HostAggregate.convert_with_links(rpc_aggregate)


    #@policy.authorize_wsgi('mogan:aggregate', 'create')
    @expose.expose(HostAggregate, body=HostAggregate,
                   status_code=http_client.CREATED)
    def post(self, aggregate):
        """create a new host aggregate
        param aggregate: a aggregate within the request body.
        """
        new_aggregate = objects.Aggregate(pecan.request.context,
                                    **aggregate.as_dict())
        new_aggregate.create()
        # Set the HTTP Location Header
        pecan.response.location = link.build_url('aggregates',
                                                 new_aggregate.uuid)
        return HostAggregate.convert_with_links(new_aggregate)


    #@policy.authorize_wsgi('mogan:aggregate', 'delete')
    @expose.expose(None, types.uuid, status_code=http_client.NO_CONTENT)
    def delete(self, aggregate_uuid):
        """delete a host aggregate
        param aggregate_uuid: UUID of an aggregate
        """
        rpc_aggregate = objects.Aggregate.get(pecan.request.context, aggregate_uuid)
        rpc_aggregate.destroy()


    #@policy.authorize_wsgi('mogan:aggregate', 'update')
    @expose.expose(HostAggregate, types.uuid, body=HostAggregate)
    def put(self, aggregate_uuid, aggregate):
        """update a host aggregate
        :param aggregate_uuid: the uuid of the aggregate to be updated.
        :param aggregate: a aggregate within the request body
        """

        try:
            aggregate_in_db = objects.Aggregate.get(
                pecan.request.context, aggregate_uuid)
        except exception.AggregateNotFound:
            msg = (_("Aggregate %s could not be found") %
                   aggregate_uuid)
            raise wsme.exc.ClientSideError(
                msg, status_code=http_client.BAD_REQUEST)
        need_to_update = False
        for attr in ('name', 'availibality_zone'):
            if getattr(aggregate, attr) != wtypes.Unset and attr=='name':
                need_to_update = True
                setattr(aggregate_in_db, attr, getattr(aggregate, attr))
            if getattr(aggregate, attr) != wtypes.Unset:
                setattr(aggregate_in_db, attr, getattr(aggregate, attr))
        # don't need to call db_api if no update
        if need_to_update:
            aggregate_in_db.save()
        # Set the HTTP Location Header
        pecan.response.location = link.build_url('aggregate',
                                                 aggregate_in_db.uuid)
        return HostAggregate.convert_with_links(aggregate_in_db)
