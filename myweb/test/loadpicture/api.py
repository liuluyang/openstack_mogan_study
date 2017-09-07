#coding:utf8

from multiprocessing import Pool
import os, time, random
import threading
from gevent import monkey;monkey.patch_all()   #此项跟多进程有冲突
from gevent.pool import Pool as gevent_pool
import gevent

from myweb.test.process_and_thread.func_timelimit import timelimit
from myweb.test.loadpicture.save_picture import make_url, load_image
from myweb.test.run_time import run_time

#loading image by process 20s
@run_time
def main():
    print 'parent process %s'%(os.getpid())
    p = Pool()
    for i in range(100):
        url = make_url(start_num=490000, index=i)
        p.apply_async(timelimit, args=(11, load_image), kwds={'args':(url,)})
    print 'waiting for all subprocess done '
    p.close()
    p.join()
    print 'all done!'

#loading image by threading  10s
@run_time
def main_thread():
    for i in range(100):
        url = make_url(start_num=490000, index=i)
        t = threading.Thread(target=load_image, args=(url,))
        t.start()

    print 'all done!'

@run_time
def main_gevent():
    urls = [gevent.spawn(load_image, make_url(start_num=490000, index=i)) for i in range(100)]
    gevent.wait(urls)

if __name__ == '__main__':
    #main()
    main_thread()
    #main_gevent()



