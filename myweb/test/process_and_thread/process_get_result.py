#coding:utf8
from multiprocessing import Pool
import time

def mul(x, y):
    time.sleep(1)
    return x*y

if __name__ == '__main__':
    start = time.time()
    p = Pool()
    _list = []
    for i in range(5):
        p1 = p.apply_async(mul, args=(i, i+1))
        _list.append(p1)

    p.close()
    #p.join()    #此时这条语句加不加一样 会等待程序结束 返回结果
    print p1.get()
    print _list
    for i in _list:
        print i.get()
    end = time.time()
    print 'end'
    print end-start