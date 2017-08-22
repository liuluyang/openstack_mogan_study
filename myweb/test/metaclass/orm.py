class Field(object):
    def __init__(self, name, column_type=None):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return 'name:%s,column_type:%s'%(self.name,self.__class__.__name__)

name = Field('name',str)
print name

class InterField(Field):
    def __init__(self, name):
        super(InterField, self).__init__(name )

id = InterField('uuid')
print id.column_type

class TeMetaclass(type):
    def __new__(cls, name, bases, attrs):
        #attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

#print TeMetaclass.__class__
#print TeMetaclass.__bases__

class Te(str):
    __metaclass__ = TeMetaclass

    #def __init__(self, name):
        #self.name = name
    #def __str__(self):
        #return self.name
    def __add__(self, other):
        return str(other)+str(self)


class Techild(Te):
    def tech(self):
        pass

te = Te('hossk')
print te.__class__

def su():
    def te():
        print 1

    return Techild


su = su()
print type(su)

print Te('ss')+Te('33')

import abc

import six
@six.add_metaclass(abc.ABCMeta)
class Base(object):
     #__metaclass__ = abc.ABCMeta


     @abc.abstractmethod
     def value(self):
         return 'not get this value'

     def key(self, k):
         self.k ='g'+k
         print 'i am father key'
         return 'not get this key'

#Base._abc_invalidation_counter =3
print Base._abc_invalidation_counter
print Base

class API(Base):

    stack = 'iz stack'


    def value(self):
        return 'this is name'
    def key(self, k='None'):
        super(API, self).key(k)
        #print data
        print self.k
        return 'get this key'
api = API()
print type(api.key)
setattr(api,'ke','None')
print api.ke

import types

class _C():
    def _m(self):
        pass

print type(_C)
print types.ClassType
print '#'*20
print types.IntType
print types.InstanceType
_c = _C()
print type(_c._m)
print types.MethodType
all_types = types.__all__
for type_name in all_types:
    print type_name
print '#'*20
print type(globals)
for i,value in globals().items():
    print i,value

print type(six.text_type)

class Test(object):
     #__class__ = 'f'
     __bases__ = 1
     def __init__(self):
         pass


print Test.__class__,'Test'
print Test().__bases__