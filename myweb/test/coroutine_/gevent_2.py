from gevent import monkey; monkey.patch_all()
import gevent
import urllib2
from gevent.pool import Pool

def f(url):
    print('GET: %s' % url)
    resp = urllib2.urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))
'''
gevent.joinall([
        gevent.spawn(f, 'https://www.python.org/'),
        gevent.spawn(f, 'https://www.baidu.com/'),
        gevent.spawn(f, 'https://github.com/'),
])
'''
url = ['https://www.python.org/','https://www.baidu.com/','https://github.com/','https://www.baidu.com/',]
p = Pool(10)
#p.map(f, url)
urls = [gevent.spawn(f,i) for i in url]
gevent.wait(urls)