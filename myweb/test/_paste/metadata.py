class Metadata(object):
    def __init__(self, in_args):
        self.in_args = in_args

    def __call__(self, environ, start_response):
        print environ['user_id']
        start_response('200 ok', [('Content-Type','application/json')])
        return '{"name":"metadata"}'

    @classmethod
    def app_factory(cls, global_config, in_args):
        return cls(in_args)

#def app_factory(global_config, in_args):
    #return Metadata(in_args)


class Cors(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        environ['user_id'] = 1234
        return self.app(environ, start_response)

    @classmethod
    def filter_factory(cls, app, global_config):
        return cls(app)

#def filter_factory(app, global_config):
    #return Cors(app)