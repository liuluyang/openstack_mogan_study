from oslo_db import exception as db_exc
from oslo_log import log as logging
from oslo_versionedobjects import base as object_base

from myweb.db import api_myweb
from myweb import objects
from myweb.objects import base
from myweb.objects import fields as object_fields

OPTIONAL_FIELDS = ['metadata', 'hosts']


LOG = logging.getLogger(__name__)

@base.MoganObjectRegistry.register
class Aggregate(base.MoganObject, object_base.VersionedObjectDictCompat):
    # Version 1.0: Initial version
    VERSION = '1.0'

    dbapi = api_myweb.Connection()

    fields = {
        'uuid': object_fields.UUIDField(nullable=True),
        'name': object_fields.StringField(nullable=True),
        'availability_zone': object_fields.StringField(nullable=True),
        'metadata': object_fields.FlexibleDictField(),
        'hosts': object_fields.ListOfStringsField(),
    }

    def __init__(self, *args, **kwargs):
        super(Aggregate, self).__init__(*args, **kwargs)
        self._orig_metadata = {}
        self._orig_hosts = {}

    @staticmethod
    def _from_db_object(context, aggregate, db_aggregate, expected_attrs=None):
        if expected_attrs is None:
            expected_attrs = []

        for name, field in aggregate.fields.items():
            if name in OPTIONAL_FIELDS:
                continue
            value = db_aggregate[name]
            if isinstance(field, object_fields.IntegerField):
                value = value if value is not None else 0
            aggregate[name] = value

        if 'metadata' in expected_attrs:
            aggregate.metadata = db_aggregate['metadata']

        if 'hosts' in expected_attrs:
            aggregate._load_hosts(context)

        aggregate.obj_reset_changes()
        return aggregate

    def _load_hosts(self, context):
        self.hosts = [x['host_id'] for x in
                         self.dbapi.aggregate_host_get(context, self.uuid)]
        self.obj_reset_changes(['hosts'])

    def obj_reset_changes(self, fields=None, recursive=False):
        super(Aggregate, self).obj_reset_changes(fields=fields,
                                              recursive=recursive)
        if fields is None or 'metadata' in fields:
            self._orig_metadata = (dict(self.metadata)
                                      if self.obj_attr_is_set('metadata')
                                      else {})
        if fields is None or 'hosts' in fields:
            self._orig_hosts = (list(self.hosts)
                                   if self.obj_attr_is_set('hosts')
                                   else [])

    def obj_what_changed(self):
        changes = super(Aggregate, self).obj_what_changed()
        if ('metadata' in self and
                self.metadata != self._orig_metadata):
            changes.add('metadata')
        if 'hosts' in self and self.hosts != self._orig_hosts:
            changes.add('hosts')
        return changes


    @staticmethod
    def _from_db_object_list(db_objects, cls, context):
        """Converts a list of database entities to a list of formal objects."""
        return [Aggregate._from_db_object(context, cls(context), obj,
                                       expected_attrs=['metadata'])
                for obj in db_objects]

    @classmethod
    def list(cls, context):
        """Return a list of Aggregate objects."""
        db_aggregates = cls.dbapi.aggregate_get_all(context)
        return Aggregate._from_db_object_list(db_aggregates, cls, context)

    @classmethod
    def get(cls, context, aggregate_uuid):
        """Find a Aggregate and return a Aggregate object."""
        db_aggregate = cls.dbapi.aggregate_get(context, aggregate_uuid)
        aggregate = Aggregate._from_db_object(
            context, cls(context), db_aggregate,
            expected_attrs=['metadata', 'hosts'])
        return aggregate

    def create(self, context=None):
        """Create a Aggregate record in the DB."""
        values = self.obj_get_changes()
        db_flavor = self.dbapi.aggregate_create(context, values)
        self._from_db_object(context, self, db_flavor,
                             expected_attrs=['metadata'])

    def destroy(self, context=None):
        """Delete the Aggregate from the DB."""
        self.dbapi.aggregate_destroy(context, self.uuid)
        self.obj_reset_changes()

    def save(self, context=None):
        updates = self.obj_get_changes()
        hosts = updates.pop('hosts', None)
        metadata = updates.pop('metadata', None)
        if metadata is not None:
            deleted_keys = (set(self._orig_metadata.keys()) -
                            set(metadata.keys()))
            added_keys = self.metadata
        else:
            added_keys = deleted_keys = None

        if hosts is not None:
            deleted_hosts = set(self._orig_hosts) - set(hosts)
            added_hosts = set(hosts) - set(self._orig_hosts)
        else:
            added_hosts = deleted_hosts = None

        if added_keys or deleted_keys:
            self.save_metadata(context, self.metadata, deleted_keys)

        if added_hosts or deleted_hosts:
            self.save_hosts(context, added_hosts, deleted_hosts)

        self.dbapi.aggregate_update(context, self.uuid, updates)

    def save_metadata(self, context, to_add=None, to_delete=None):
        """Add or delete metadata.

        :param:to_add: A dict of new keys to add/update
        :param:to_delete: A list of keys to remove
        """
        ident = self.uuid

        to_add = to_add if to_add is not None else {}
        to_delete = to_delete if to_delete is not None else []

        if to_add:
            self.dbapi.metadata_update_or_create(context, ident, to_add)

        for key in to_delete:
            self.dbapi.aggregate_metadata_delete(context, ident, key)
        self.obj_reset_changes(['metadata'])

    def save_hosts(self, context, to_add=None, to_delete=None):
        """Add or delete hosts.

        :param:to_add: A list of hosts to add
        :param:to_delete: A list of hosts to remove
        """
        ident = self.uuid

        to_add = to_add if to_add is not None else []
        to_delete = to_delete if to_delete is not None else []

        for host_id in to_add:
            self.dbapi.aggregate_host_add(context, ident, host_id)

        for host_id in to_delete:
            self.dbapi.aggregate_host_remove(context, ident, host_id)
        self.obj_reset_changes(['hosts'])



