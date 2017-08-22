from pecan import rest
from wsme import types as wtypes

from myweb.api import expose
from myweb.api.controllers.v1 import users as v1_users
from myweb.api.controllers.v1 import host_aggregate as node_aggregate

class V1Controller(rest.RestController):
    users = v1_users.UsersController()
    aggregates = node_aggregate.AggregateController()

    @expose.expose(wtypes.text)
    def get(self):
        print 'I am v1'
        return 'helle I am V1'