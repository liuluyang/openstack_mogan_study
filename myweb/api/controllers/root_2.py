from pecan import rest
from wsme import types as wtypes

from myweb.api.controllers.v1 import types, controller
from myweb.api.controllers import base
from myweb.api import expose



class Root(base.APIBase):
    name = wtypes.text
    desc = wtypes.text

    @staticmethod
    def convert():
        root = Root()
        root.name = 'this is openstack mogan api'
        root.desc = 'this is mogan api desc'
        return root


class RootController(rest.RestController):
    _custom_actions = {
        'bool': ['GET']
    }

    v1 = controller.V1Controller()

    @expose.expose(Root)
    def get(self):
        return Root.convert()

    @expose.expose(wtypes.text)
    def bool(self):
        return 'this is bool'

    @expose.expose(wtypes.text, wtypes.text)
    def get_one(self, id):
        return id
