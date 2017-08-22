#coding:utf8

import multiprocessing, threading
from multiprocessing import Process
#import os
def dead_line(n):
    while True:
        n = n + 1
        print n,#os.getpid()#threading.current_thread().name


for i in range(multiprocessing.cpu_count()):
    #t = threading.Thread(target=dead_line, args=(i,))
    #t.start()
    p = Process(target=dead_line, args=(i,))
    p.start()