#coding:utf8
import functools

def add_kws(*args, **kwargs):
    print '1@decorator(add_kws) args:',args
    def wrapper(f):
        #@functools.wraps(f)#注释掉装饰器查看stu.__name__的变化
        def add(*args, **kwargs):
            print '1@func(add) agrs',args
            print '1@__name__:',f.__name__
            kwargs['add_kws'] = 'add_val'
            return f(*args, **kwargs)
        return add
    return wrapper

def validate_result(*args, **kwargs):
    print "#"*20
    print '2@decorator(validate) args:',args
    def wrapper(f):
        #@functools.wraps(f)
        def add_(*args, **kwargs):
            print '2@func(add_) agrs',args
            print '2@__name__:',f.__name__
            kwargs['validate_'] = 'add_val'
            fun = f(*args, **kwargs)
            print 'return fun result:',fun
            fun['age'] = 12
            return fun
        return add_
    return wrapper

@add_kws('d')
@validate_result('v')
def stu(name, age, **kwargs):
    print kwargs
    print 'name:',name
    print 'age:',age
    return {'name':'xiaoli'}

st = stu('xiaoming', 12)

print st
print 'stu.__name__:',stu.__name__
#
