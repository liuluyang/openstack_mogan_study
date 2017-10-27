import gevent
from gevent.queue import Queue
products = Queue()
def consumer(name):
    while not products.empty():
        print '%s got product %s' % (name, products.get())
        gevent.sleep(0)
    print '%s Quit'
def producer():
    for i in xrange(1, 10):
        products.put(i)
gevent.joinall([
    gevent.spawn(producer),
    gevent.spawn(consumer, 'steve'),
    gevent.spawn(consumer, 'john'),
    gevent.spawn(consumer, 'nancy'),
])
