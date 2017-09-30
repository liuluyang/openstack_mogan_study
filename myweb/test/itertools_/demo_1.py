# coding:utf8

import itertools

r = itertools.count(1)
print r
for i in r:
    print i
    if i == 10:
        break

c = itertools.cycle('abc')
print c
count = 0
for i in c:
    print i
    if i == 'c':
        count += 1
    if count == 2:
        break

g = itertools.groupby('sfffesjes')
for key, value in g:
    print key, list(value) ,value
print '#'*20
gb = itertools.groupby('aAAsADSAAdad', lambda x:x.upper())
for key, group in gb:
    print key, list(group)

m  = itertools.imap(lambda x:x*2, [1,2,3])
print m, next(m)
for i in m:
    print i

