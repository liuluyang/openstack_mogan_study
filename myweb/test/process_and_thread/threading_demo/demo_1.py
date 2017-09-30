#coding:utf8

import os, time, threading

def task(n):
    print 'threading %s running : %s'%(threading.current_thread(), n)

for i in range(4):
    #print 'start threading ',threading.current_thread()
    p = threading.Thread(target=task, args=(i,))
    p.start()

print 'end'
