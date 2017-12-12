import pecan
from pecan import rest
from wsme import types as wtypes
from myweb.api.controllers import base
from myweb.api import expose
from myweb.api.controllers.v1 import controller as v1_controller


class Root(base.APIBase):

    name = wtypes.text
    """The name of the API"""

    description = wtypes.text
    """Some information about this API"""

    @staticmethod
    def convert():
        root = Root()
        root.name = "OpenStack Mogan API"
        root.description = ("Mogan is an OpenStack project which aims to "
                            "facilitate baremetal machines management.")
        return root

class RootController(rest.RestController):

    _custom_actions = {
        'test':['GET']
    }

    _versions = ['v1']
    _default_version = 'v1'

    v1 = v1_controller.V1Controller()

    @expose.expose(Root)
    def get(self):
        return Root.convert()

    @expose.expose(wtypes.text)
    def test(self):
        return "hello I am test"

    @expose.expose(wtypes.text)
    def _default(self):
        return 'default'

    # @pecan.expose()
    # def _route(self, args):
    #     """Overrides the default routing behavior.
    #
    #     It redirects the request to the default version of the mogan API
    #     if the version number is not specified in the url.
    #     """
    #     print args
    #     print 'this is _route'
    #     if args[0] and args[0] not in self._versions:
    #         args = [self._default_version] + args
    #         print args
    #     return super(RootController, self)._route(args)
