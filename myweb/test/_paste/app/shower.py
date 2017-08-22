class Shower(object):
    def __init__(self, in_arg):
        self.in_arg = in_arg

    def __call__(self, environ, start_response):
        print 'Shower'
        for i in environ:
            print i
        start_response('200 ok', [('Content Type', 'text/plain')])
        return ['%s, %s!\n' % (self.in_arg, 'Shower')]

def app_factory(global_config, in_arg):
    print 'shower',global_config
    return Shower(in_arg)