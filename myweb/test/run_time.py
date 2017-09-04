#coding:utf8

import time, functools
from myweb.test._oslo_log.olso_log_test import LOG
def run_time(f):
    @functools.wraps(f)
    def wapper(*args, **kwargs):
        #print args
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        LOG.info('Running time %s'%(end-start))
        return result
    return wapper

@run_time
def dex(x, y):
    time.sleep(2)
    return x+y
if __name__ == '__main__':
    dex(2,3)