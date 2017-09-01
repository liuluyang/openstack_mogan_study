#coding:utf8

from multiprocessing import Pool, Process, Queue
import os, time, random
'''
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
'''

# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        #time.sleep(random.random())

def write_2(q):
    print('Process to write: %s' % os.getpid())
    for value in ['D', 'E', 'F']:
        print('Put %s to queue...' % value)
        q.put(value)
        print q.qsize()
        #time.sleep(random.random())
# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        time.sleep(random.random())
        value = q.get(True)
        print('Get %s from queue.' % value)

def read_2(q):
    print('Process to read: %s' % os.getpid())
    num = 0
    while num<3:
        #time.sleep(random.random())
        value = q.get(True)
        num +=1
        print('Get %s from queue.' % value),os.getpid()

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    start = time.time()
    q = Queue()
    ww = Process(target=write_2, args=(q,))
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pp = Process(target=read_2, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    ww.start()
    # 启动子进程pr，读取:
    time.sleep(0.2)
    print '###queue:',q.qsize()
    pr.start()
    pp.start()
    # 等待pw结束:
    pw.join()
    ww.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    time.sleep(3)
    pr.terminate()
    pp.terminate()
    end = time.time()
    print '%0.2f'%(end-start)