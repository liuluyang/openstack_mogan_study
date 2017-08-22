from oslo_versionedobjects import base as object_base

#from mogan.db import api as dbapi
from myweb.objects import base
from myweb.objects import fields as object_fields


OPTIONAL_FIELDS = ['extra_specs', 'projects']


@base.MoganObjectRegistry.register
class User(base.MoganObject, object_base.VersionedObjectDictCompat):
    # Version 1.0: Initial version
    VERSION = '1.0'

    #dbapi = dbapi.get_server()

    fields = {
        'id': object_fields.IntegerField(read_only=True, nullable=True),
        'user_id': object_fields.StringField(nullable=True),
        'name': object_fields.StringField(nullable=False),
        'email': object_fields.StringField(nullable=True),
        'extra': object_fields.FlexibleDictField(),
        'like': object_fields.ListOfStringsField(),
    }

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
