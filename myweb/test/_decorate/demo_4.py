#coding:utf8

from contextlib import contextmanager


@contextmanager
def b_a(b, a):
    print b
    yield 1
    print a

with b_a('before', 'after') as f:
    print f
    print 'hello'
