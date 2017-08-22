class DrinkingFountain(object):
    def __init__(self, in_arg):
        self.in_arg = in_arg

    def __call__(self, environ, start_response):
        print 'DrinkingFountain'
        start_response('200 ok', [('Content Type', 'text/plain')])
        return ['%s, %s!\n' % (self.in_arg, 'DrinkingFountain')]

def app_factory(global_config, in_arg):
    print 'drinking_fountain',global_config
    return DrinkingFountain(in_arg)