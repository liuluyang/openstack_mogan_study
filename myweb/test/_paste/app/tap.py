import webob

class Tap(object):
    def __init__(self, **in_arg):
        self.in_arg = in_arg
        print in_arg

    def __call__(self, environ, start_response):
        print environ
        for i,z in environ.items():
            print (i.lower(),z)
        print 'Tap'
        #if True:
            #raise webob.exc.HTTPForbidden
        start_response('200 ok', [('Content-Type', 'application/json')])
        #return ['%s, %s!\n' % (self.in_arg, 'Tap')]
        return '{"NAME":"hello"}'

def app_factory(global_config, **in_arg):
    print 'tap',global_config
    for i,z in global_config.items():
        print (i,z)
    print in_arg
    return Tap()