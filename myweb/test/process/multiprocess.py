#coding:utf8

import threading

num = 0
lock = threading.Lock()
def change_it(n):
    global num
    num = num + n
    num = num - n

def thread_run(n):
    for i in range(10000):
        lock.acquire()
        change_it(n)
        lock.release()

if __name__ == '__main__':
    p1 = threading.Thread(target=thread_run, args=(2,))
    p2 = threading.Thread(target=thread_run, args=(3,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print num