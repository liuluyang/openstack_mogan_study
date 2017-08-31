#coding:utf8
#class TimeLimitExpired(Exception): pass
from myweb.test._oslo_log.olso_log_test import LOG

import threading
class FuncThread(threading.Thread):
    #_outtime_nums = 0
    def __init__(self, func, args, kws):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.kws = kws
        self.result = None
        #FuncThread._outtime_nums +=1

    def run(self):
        self.result = self.func(*self.args, **self.kws)

    def _stop(self):
        if self.isAlive():
            threading.Thread._Thread__stop(self)

def timelimit(timeout, func, args=(), kwargs={}):
    """ Run func with the given timeout. If func didn't finish running
        within the timeout, raise TimeLimitExpired
    """
    it = FuncThread(func, args, kwargs)
    #print it._outtime_nums
    it.start()
    it.join(timeout)
    if it.isAlive():
        it._stop()
        #raise TimeLimitExpired()
        LOG.error('this process running time is out!')
        #LOG.error('the nums of outtime processes are %s'%it._outtime_nums)
    else:
        #it._outtime_nums -=1
        return it.result

def fn():
    #while True:
        #a = 1
    print 1
#if __name__ == '__main__':
#timelimit(3, fn)