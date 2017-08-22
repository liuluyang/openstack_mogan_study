#coding:utf8


import threading, time, random

def loop():
    print 'the threading is %s'%(threading.current_thread().name)

    for i in range(5):
        time.sleep(random.random())
        print random.random()
        print 'the threading is %s >>>%s'%(threading.current_thread().name, i)

    print 'threading ended %s'%(threading.current_thread().name)


if __name__ == '__main__':
    print 'the threading is %s'%(threading.current_thread().name)
    p = threading.Thread(target=loop, name='Loopthreading')
    p.start()
    p.join()
    print 'threading ended %s'%(threading.current_thread().name)
