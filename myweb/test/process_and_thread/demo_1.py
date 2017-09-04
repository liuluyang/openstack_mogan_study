#coding:utf8

from multiprocessing import Process, Queue, Pool
import time, random

from myweb.test.run_time import run_time

def task(num, q):
    n = num*10
    for i in range(10):
        time.sleep(random.random())
        q.put(n+i)

def main_1():
    q = Queue()
    _list = []
    for i in range(4):
        p = Process(target=task, args=(i, q))
        _list.append(p)
    for i in _list:
        i.start()
    for i in _list:
        i.join()
    for i in range(q.qsize()):
        print q.get()


def task_2(num):
   # time.sleep(random.random())
    time.sleep(2)
    print num*2
    return num*2

@run_time
def main_2():
    p = Pool(4)
    r = p.map(task_2, [1,2,3,4,5,6])
    print r


if __name__ == '__main__':
    #main_1()
    main_2()