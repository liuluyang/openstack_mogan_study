#coding:utf8

from wsgiref.simple_server import make_server
from routes import Mapper,middleware
from routes import Mapper, middleware
from webob import Response, Request
from webob import Request,Response
import webob.dec
import webob.exc
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

        return self.router

    @staticmethod
    @webob.dec.wsgify
    def dispatch(req):
        match = req.environ['wsgiorg.routing_args'][1]
        if not match:
            return webob.exc.HTTPNotFound()
        app = match['controller']
        print match

        return app(req, **match)

def app_factory(global_config, **in_arg):

    return Router()

class UsersController(object):

    @webob.dec.wsgify
    def index(self, req):
        return Response('xiaoming')

    @webob.dec.wsgify
    def show(self, req, id):
        return Response(id)

class Router_(object):
    def __init__(self):
        self.mapper = Mapper()
        self.Router = middleware.RoutesMiddleware(self._dispatch, self.mapper)

        self.mapper.connect('/xiaoming', controller=UsersController(), action='index', conditions={'method':['GET']})
        self.mapper.connect('/xiaoming/{id}', controller=UsersController(), action='show', conditions={'method':['GET']})
    @webob.dec.wsgify
    def __call__(self, req):
        return self.Router

    @staticmethod
    @webob.dec.wsgify
    def _dispatch(req):
        match = req.environ['wsgiorg.routing_args'][1]
        if not match:
            return webob.exc.HTTPNotFound()
        app = match['controller']
        return app

    @classmethod
    def factory(cls, global_config):
        return cls()