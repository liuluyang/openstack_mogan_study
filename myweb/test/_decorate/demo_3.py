#coding:utf8

import threading
import itertools
from decorator import decorator
import time

class Future(threading.Thread):
    """
    A class converting blocking functions into asynchronous
    functions by using threads.
    """
    def __init__(self, func, *args, **kw):
        try:
            counter = func.counter
        except AttributeError:  # instantiate the counter at the first call
            counter = func.counter = itertools.count(1)
        name = '%s-%s' % (func.__name__, next(counter))
        print name

        def func_wrapper():
            self._result = func(*args, **kw)
        super(Future, self).__init__(target=func_wrapper, name=name)
        self.start()

    def result(self):
        self.join()
        return self._result

@decorator(Future)
def long_running(x):
    time.sleep(x)
    return x
start = time.time()
f1 = long_running(1)
#long_running.counter = 2
#print long_running.counter
#print next(itertools.count(22))
f2 = long_running(2)
print 'threading time'
r = f1.result()+f2.result()
print r
end = time.time()
print end-start