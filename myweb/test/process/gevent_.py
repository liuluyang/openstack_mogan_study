#coding:utf8


from gevent import monkey; monkey.patch_all()
import gevent
import urllib2
import time



def f(url):
    print('GET: %s' % url)
    resp = urllib2.urlopen(url)
    time.sleep(2)
    data = resp.read()
    #if len(data)>=460000:
        #print data
    print('%d bytes received from %s.' % (len(data), url))
    global start
    print time.time()-start



start = time.time()
'''
gevent.joinall([
        gevent.spawn(f, 'https://baidu.com'),
        gevent.spawn(f, 'https://baidu.com'),
        gevent.spawn(f, 'https://baidu.com'),
])

url_list = ['https://baidu.com', 'https://baidu.com','https://baidu.com']

print '#'*20
start_2 = time.time()
print 'start for ....'
for i in url_list:
    f(i)
print time.time()-start_2

print '#'*20
'''
from multiprocessing import Process

start_3 = time.time()

if __name__ == '__main__':
    p1 = Process(target=f, args=('https://baidu.com',))
    p2 = Process(target=f, args=('https://baidu.com',))
    p3 = Process(target=f, args=('https://baidu.com',))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()


print time.time()-start_3
