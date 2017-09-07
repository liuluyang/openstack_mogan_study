#coding:utf8

def dex(n=0):
    print 'init generator function dex'
    while True:
        print 'print n'
        print 'next'
        n +=1
        r = yield n
        #r = 2
        print '#'*12
        print r
d = dex()


print d.next()
'''
print d.next()
print d.next()
print next(d)
print d.send(8)
print d.send(8)
print d.send(['f'])
'''