class Purifier(object):
    def __init__(self, app, in_arg, global_config):
        self.app = app
        self.in_arg = in_arg

    def __call__(self, environ, start_response):
        print 'Purifier'
        #print app
        return self.app(environ, start_response)

def filter_factory(app, global_config, in_arg):
    return Purifier(app, in_arg, global_config)