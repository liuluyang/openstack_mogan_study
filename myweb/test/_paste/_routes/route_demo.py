#coding:utf8

from wsgiref.simple_server import make_server
from routes import Mapper,middleware
from webob import Request,Response
import webob.dec
import webob.exc

class Controller(object):
    #@webob.dec.wsgify
    #def __call__(self, req):
        #return Response("Hello World!")
    @webob.dec.wsgify
    def index(self, req, **kwargs):
        return Response('index')
    @webob.dec.wsgify
    def show(self, req, id, **kwargs):
        print req
        return Response('show'+str(id))



class Router(object):
    def __init__(self):
        self.mapper = Mapper()

        #self.mapper.resource('li','lis', controller=Controller)
        self.router = middleware.RoutesMiddleware(self.dispatch, self.mapper) #创建实例，调用的时候进行路由匹配，修改环境变量
        self.mapper.connect('/lixin',controller=Controller().index, action='index',conditions={'method': ['GET']})
        self.mapper.connect('/lilin/{id}',controller=Controller().show, action='show',conditions={'method': ['GET']})

    @webob.dec.wsgify
    def __call__(self, req):

        urll = ['%s : %s' % (k,v) for k,v in sorted(req.environ.items())]
        print '\n'.join(urll) #原始的环境变量
        print '#'*20
        return self.router

    @staticmethod
    @webob.dec.wsgify
    def dispatch(req):
        urll = ['%s : %s' % (k,v) for k,v in sorted(req.environ.items())]
        print '\n'.join(urll)   #从这里可以看出来环境变量已经改变了
        match = req.environ['wsgiorg.routing_args'][1]
        print '$$$$$$',match

        if not match:
            return webob.exc.HTTPNotFound()

        app = match['controller']

        return app(req, **match)

def app_factory(global_config, **in_arg):

    return Router()

#app = Router()
#print app
#print 'Listen port on 8003'
#httpd = make_server('localhost', 8003, app)
#httpd.serve_forever()

class Router_2(object):
    def __init__(self):
        self.maper = Mapper()
        self.maper.connect('/users', controller=Controller(), action='index', conditions={'method':['GET']})
        self.router = middleware.RoutesMiddleware(self._dispatch, self.maper)

    @webob.dec.wsgify
    def __call__(self,req):
        return self.router


    @webob.dec.wsgify
    def _dispatch(req):
        match = req.environ['wsgiorg.routing_args'][1]
        if not match:
            return webob.exc.HTTPNotFound
        app = match['controller']
        return app
