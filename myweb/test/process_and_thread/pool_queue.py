#coding:utf8

from multiprocessing import Pool, Queue
import time, random

def run_task(i, q):
    time.sleep(random.random())
    #q.put(i)
    print i

if __name__ == '__main__':
    #q = Queue()
    p = Pool()
    #q = Queue()
    q = 1
    for i in range(5):
        p.apply_async(run_task, args=(i, q))
    p.close()
    p.join()
    print 'end'
