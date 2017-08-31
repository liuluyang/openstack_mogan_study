#coding:utf8

from multiprocessing import Pool, Queue
import os, time, random

from func_timelimit import timelimit


def run_task(name, dic):
    print '>>running subprocess %s %s'%(name, os.getpid())
    start = time.time()
    t = random.random()*5
    #q.put(t)
    print '%s %s seconds'%(name, t)
    dic[str(name)] = t
    print dic
    time.sleep(t)
    end = time.time()
    print '$<<task %s runs %0.2f seconds '%(name, end-start)
    return True


def test():
    print 'parent process %s'%(os.getpid())
    dic = {}
    p = Pool()
    for i in range(5):
        p.apply_async(timelimit, args=(1,run_task), kwds={'args':(i,dic)})
    print 'waiting for all subprocess done '
    p.close()
    p.join()
    print 'all done!'
    print dic #{}


if __name__ == '__main__':
    test()



