import os
from paste.deploy import loadapp
from wsgiref.simple_server import make_server

class Portal():
    def __init__(self):
        pass

    def __call__(self,environ,start_response):
        start_response("200 OK",[("Content-type", "text/plain")])
        return ["Paste Deploy Blog Protal: Version = 1.0.0",]

    @classmethod
    def factory(cls,global_conf,**kwargs):
        print "in Protal.factory", global_conf, kwargs
        return Portal()

class AdminWeb():
    def __init__(self):
        pass

    def __call__(self,environ,start_response):
        start_response("200 OK",[("Content-type", "text/plain")])
        return ["Paste Deploy Blog Admin: Version = 1.0.0",]

    @classmethod
    def factory(cls,global_conf,**kwargs):
        print "in Admin.factory", global_conf, kwargs
        return AdminWeb()

#Filter
class LogFilter():
    def __init__(self,app):
        self.app = app
        pass
    def __call__(self,environ,start_response):
        print "filter:LogFilter is called."
        return self.app(environ,start_response)

    @classmethod
    def factory(cls, global_conf, **kwargs):
        print "in LogFilter.factory", global_conf, kwargs
        return LogFilter

if __name__ == '__main__':
    configfile="log_conf.ini"
    appname="blog"
    wsgi_app = loadapp("config:%s" % os.path.abspath(configfile), appname)
    server = make_server('0.0.0.0',8001,wsgi_app)
    server.serve_forever()
    pass