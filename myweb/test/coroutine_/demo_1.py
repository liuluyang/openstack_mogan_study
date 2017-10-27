# -*- coding: utf-8 -*-

import time

def consumer():
    r = 'gg'
    print 'entry consumer'
    while True:
        n = yield r
        print 'n:',n
        #if not n:
            #return
        #time.sleep(1)
        print('[CONSUMER] Consuming %s...' % n)
        time.sleep(2)
        r =n #'200 OK'

def produce(c):
    print c.send(None)
    print 'after s.send()'
    n = 0
    while n < 5:

        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        n = n + 1
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)