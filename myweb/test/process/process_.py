#coding:utf8

from multiprocessing import Process
import os

def _run(name):
    print '_run func is running ... name:%s  pid:%s'%(name,os.getpid())


if __name__ == '__main__':
    print 'parent process is running %s'%(os.getpid())

    p = Process(target=_run, args=('test',))
    p.start()
    p.join()
    print 'end'
