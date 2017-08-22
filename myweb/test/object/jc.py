#coding:utf8

class Base(object):
    basetype = None
    basename = None

    def __init__(self,name,leve):
        self._name = name
        self._leve = leve

    def name(self):
        print 'Base obj basename:',Base.basename,self.basename
        return self._name

    def leve(self):
        return self._leve

class User(Base):
    basetype = str
    basename = 'user'

    def fun(self):
        return 'fun obj'

class Text(Base):
    basetype = str
    basename = 'text'

    def __init__(self,name=None,leve=None,other=None):
        super(Text,self).__init__(name,2)
        self.leve = leve
        self._other = other

user = User
print user.__class__,user.__bases__

user = User('bob',1)
print isinstance(user, Base)
print 'user basetype:',user.basetype
print 'user name method:',user.name()
print '#'*20

text = Text()

print text.leve,text._leve
print text.name()


