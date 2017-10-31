from pecan import hooks
from pecan import hooks
from oslo_context import context
from oslo_context import context

class DBHook(hooks.PecanHook):
    """create a db connection instance"""

    def before(self, state):
        state.request.context = 'context'
        print dict(state.request.headers)
        creds = {
            'user_name': 'X-User-Name',
            'user': 'X-User-Id',
            'project_name': 'X-Project-Name',
            'tenant': 'X-Project-Id',
            'domain': 'X-User-Domain-Id',
            'domain_name': 'X-User-Domain-Name',
            'auth_token': 'X-Auth-Token',
            'roles': ['admin'],
        }

        #is_admin = policy.check('is_admin', creds, creds)
        is_admin = True
        state.request.context = context.RequestContext(
            is_admin=is_admin, **creds)
        print state.request.context

        #print 'I am hook'
        '''
        state.request.db_conn = db_api.Connection()
        #state.request.context = {'name':'lly','id':'1','is_admin':True}
        creds = {
            'user_name': 'lly',
            'user': 1,
            'project_name': 'mogan',
            'tenant': 'tenant',
            'domain': 12,
            'domain_name': 'domain_name',
            'auth_token': 'sjakfjahsfjahjkd31h14h',
            'roles': ['default','admin'],
        }

        state.request.context = context.RequestContext(
            is_admin=True, **creds)
        #print state.request.context
        faultstring = '123Traceback (most recent call last):hello world'
        traceback_marker = 'Traceback (most recent call last):'
        if faultstring and traceback_marker in faultstring:
            # Cut-off traceback.
            faultstring = faultstring.split(traceback_marker, 1)[0]
            # Remove trailing newlines and spaces if any.
            print faultstring.rstrip()

        print dict(cfg.CONF)
        print state.request.method
        print state.controller
        print state.arguments.args
        print state.arguments.varargs
        print state.arguments.keywords
        print state.hooks
        print state.request.host_url
        state.request.public_url = state.request.host_url
        print 'ok'
        '''

class ConHook(hooks.PecanHook):

    def before(self, state):
        pass





