#coding:utf8
import gevent
from gevent import monkey;monkey.patch_all()   #非阻塞
import urllib2

def op(n, url='https://www.baidu.com'):
    print 'start', n
    urllib2.urlopen(url)
    print 'end', n

g = gevent.spawn(op, 1)
g2 = gevent.spawn(op, 2)
g3 = gevent.spawn(op, 3)
#g.run()
#g2.run()
t = [g, g2, g3]
gevent.joinall(t)

