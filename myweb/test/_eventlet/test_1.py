urls = [
    "http://python.org/images/python-logo.gif",
    "http://us.i1.yimg.com/us.yimg.com/i/ww/beta/y3.gif",
]
from eventlet.greenpool import GreenPool
import eventlet
from eventlet.green import urllib2
from eventlet import greenthread


def fetch(url):
    print url
    return urllib2.urlopen(url).read()

pool = eventlet.GreenPool()
for body in pool.imap(fetch, urls):
    print("got body", len(body))

print 'end'
