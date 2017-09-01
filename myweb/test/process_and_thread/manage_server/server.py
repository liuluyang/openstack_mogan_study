from multiprocessing.managers import BaseManager
import Queue
from multiprocessing import Process
import time, random

queue = Queue.Queue()



def _dex(x, y):
    time.sleep(2)
    print x, y
    r = x*y
    return r

def dex(x, y):
    p = Process(target=_dex, args=(x, y))
    p.start()
    p.join()

    return p


class QueueManager(BaseManager):
    pass

def main():
    QueueManager.register('get_queue', callable=lambda:queue)
    QueueManager.register('dex', dex)
    m = QueueManager(address=('127.0.0.1', 9001), authkey='abc')
    s = m.get_server()
    print 'running in 9001'
    s.serve_forever()

if __name__ == '__main__':
    main()
