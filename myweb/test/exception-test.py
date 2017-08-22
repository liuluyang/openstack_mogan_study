class CustomError(Exception):
    info = 'this is Custom error'
    def __init__(self,message=None,**kwargs):
        #Exception.__init__(self)
        #self.errorinfo = info
        print id(self)
        if not message:
            message = self.info
        super(CustomError, self).__init__(message)

    def __str__(self):
        #return self.errorinfo
        return self.args[0]

try:
    #print s
    #f = open('r.r')
    raise CustomError()
    #raise NameError('name error')
except CustomError as e:
    print e
except NameError as e:
    print e
except IOError as e:
    print e


def color(name, co=None ,cc=None,*args, **kwargs):
    print name, co ,cc ,args,kwargs
#color('d',1, 2 ,d=3)


def wap_1(func):
    def new_(*args, **kwargs):
        #print func.__name__ , args #, func(*args, **kwargs)
        args +=(5,)
        print args
        #return func(*args, **kwargs)
    return new_

def wap_2(func):
    def new_2(*args, **kwargs):
        print 'i am wap_2'
        print func.__name__ , args #, func(*args, **kwargs)
        #re = func(*args, **kwargs)
        #return re*re
        return func(*args, **kwargs)
    return new_2

@wap_2
@wap_1
def sum_(a,b,*args):
    print args
    return  a+b
    #return 'd'

print sum_(1,2)
print __name__

class Bill():
    def __init__(self, text):
        self.text =text
class Duck():
    num = 1
    def __init__(self, bill):
        self.bill = bill
        self.num = 3
        Duck.num +=1
        #Duck.num = 4
    def pr(self):
        print 'this is ',self.bill.text
    @classmethod
    def count(cls):
        return cls('f')

bill = Bill('hello')
duck2 = Duck('d')
duck = Duck(bill)
duck.pr()
print duck.num
print Duck.num

print Duck.count()

class ShowStr():
    def __init__(self):
        pass
    def __str__(self):
        return  'this is str'
    def __repr__(self):
        return 'this is repr'

show = ShowStr()
show
