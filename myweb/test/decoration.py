#coding:utf8

def change(f):
    print 'this is change func'
    return f


def  decorator(funobj,*k):
    print 'is decorator'
    funobj._name = 'num'
    print funobj._name
    print k
    return change(funobj)

@decorator
class NUm(object):
    def __init__(self,*k):
        pass
        print 'is num class instance'

    def __repr__(self):
        return

    def __str__(self):
        return 'g'

num = NUm('hello')

print num

isinstance()
