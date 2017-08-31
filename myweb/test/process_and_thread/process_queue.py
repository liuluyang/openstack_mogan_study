#coding:utf8

from multiprocessing import Pool, Process, Queue
import os, time, random

q = Queue(2)
q.put(1)
q.put(2)
#try:
    #q.put(2)
#except:
    #pass
print q.get()
print q.qsize()
print q.empty()
print q.full()
print q.close()  #关闭队列
#print q