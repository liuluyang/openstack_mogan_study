from multiprocessing.managers import BaseManager
import Queue
import time

class Manager(BaseManager):
    pass

def main_client(register_name,host='127.0.0.1', port=9001, authkey='abc'):
    BaseManager.register(register_name)
    m = BaseManager(address=(host,port), authkey=authkey)
    m.connect()
    s = getattr(m, register_name)
    return s

s = main_client('get_queue')
s = s()
s.put(1)
s.put(2)
print s.qsize()
print s.get()

d = main_client('dex')
#print d(2, 34)

start = time.time()
for i in range(5):
    print d(2, 23)

end = time.time()
print end-start

