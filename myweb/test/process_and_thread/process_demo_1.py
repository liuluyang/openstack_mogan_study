#coding:utf8

from multiprocessing import Process
import os
import time

def child_process(name,num):
    time.sleep(num)
    print 'this is child process:%s %s'%(name, os.getpid())

if __name__ == '__main__':
    print 'this is parent process:',os.getpid()
    p1 = Process(target=child_process, args=('p1',3))
    p2 = Process(target=child_process, args=('p2',2))
    print 'child process will start!'
    p1.start()
    p2.start()
    #p1.join()
    p2.join() #等待执行结束 才执行后面的程序
    print 'child process is end!'