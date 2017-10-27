#coding:utf8

import random, os, time, Queue
from multiprocessing.managers import BaseManager

task_queue = Queue.Queue()
result_queue = Queue.Queue()

class Manager(BaseManager):
    pass


def main():
    Manager.register('get_task_queue', callable=lambda:task_queue)
    Manager.register('get_result_queue', callable=lambda:result_queue)
    manager = Manager(address=('127.0.0.1',9001), authkey='abc')
    #manager.start()
    manager = manager.get_server()
    manager.serve_forever()

    t = manager.get_task_queue()
    r = manager.get_result_queue()
    print t

    for i in range(10):
        t.put(i)
    for i in range(10):
        print t.get(timeout=2)

if __name__ == '__main__':
    main()


