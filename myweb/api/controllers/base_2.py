import datetime
import wsme
from wsme import types as wtypes


class APIBase(wtypes.Base):
    create_at = wsme.wsattr(datetime.datetime, readonly=True)
    updated_at = wsme.wsattr(datetime.datetime, readonly=True)

    def as_dict(self):
        return dict((k, getattr(self, k)) for k in self.fields if
                    hasattr(self, k) and getattr(self, k) != wsme.Unset)

    def unset_fields_except(self, except_list=None):

        if except_list is None:
            except_list = []

        for k in self.as_dict():
            if k not in except_list:
                setattr(self, k, wsme.Unset)
