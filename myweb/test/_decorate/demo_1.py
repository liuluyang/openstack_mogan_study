#coding:utf8
import functools

def add_kws(*args, **kwargs):
    print args
    def wrapper(f):
        @functools.wraps(f)#注释掉装饰器查看stu.__name__的变化
        def add(*args, **kwargs):
            print args
            print '__name__:',f.__name__
            kwargs['add_kws'] = 'add_val'
            return f(*args, **kwargs)
        return add
    return wrapper

@add_kws('d')
def stu(name, age, **kwargs):
    print kwargs
    print 'name:',name
    print 'age:',age
    return

st = stu('xiaoming', 12)

print st

print 'stu.__name__:',stu.__name__
#