#coding:utf8

import greenlet

def test1():
    print 12
    gr2.switch()
    print 23

def test2():
    print 22
    gr1.switch()
    print 32

gr1 = greenlet.greenlet(test1)
gr2 = greenlet.greenlet(test2)

#test1() #12 22 12 32 23
gr1.switch()  #12 22 23


def t():
    tt()
    print 1
    return 't()'

def tt():
    return 2

print t()


