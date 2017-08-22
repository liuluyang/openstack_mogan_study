class Hydrant(object):
    def __init__(self, in_arg):
        self.in_arg = in_arg

    def __call__(self, environ, start_response):
        print 'Hydrant'
        start_response('200 ok', [('Content Type', 'text/plain')])
        return ['%s, %s!\n' % (self.in_arg, 'Hydrant')]

def app_factory(global_config, in_arg):
    print 'hydrant',global_config
    return Hydrant(in_arg)