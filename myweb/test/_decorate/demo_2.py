#coding:utf8

import threading
from decorator import decorator
import time

def blocking(not_avail):
    def _blocking(f, *args, **kw):
        if not hasattr(f, "thread"):  # no thread running
            def set_result():
                f.result = f(*args, **kw)
            f.thread = threading.Thread(None, set_result)
            f.thread.start()
            return not_avail
        elif f.thread.isAlive():
            return not_avail
        else:  # the thread is ended, return the stored result
            del f.thread
            return f.result
    return decorator(_blocking)

@blocking('waiting ...')
def demo():
    #time.sleep(3)
    return 'demo'

print demo()
#?????????????question understand