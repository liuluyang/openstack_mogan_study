#coding:utf8

class Basemeta(type):
    def __new__(cls,name, bases, dict):
        print 'is creating class'
        print name,bases,dict
        return type.__new__(cls, name, bases, dict)
    def __init__(cls,name, bases, dict):
        print 'is init'

class Base(object):
    __metaclass__ = Basemeta

class te(Base):
    pass


from wsme import types as wtypes

ma = wtypes.IntegerType(1,4)

class API(wtypes.Base):
    name = wtypes.wsattr(wtypes.text, mandatory=True)
    id = int
    uuid = ma
    extra = {wtypes.text:wtypes.text}

api = API()
print api.id,api.name
print hasattr(api,'id')

print type(API.id),API.name,API.uuid,API.extra
setattr(api,'name','ff')
#del api.extra
print api.name
del API.name
for i,v in API.__dict__.iteritems():
    print i,'--',v



