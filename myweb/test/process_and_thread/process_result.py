#coding:utf8

from  multiprocessing import Process

class MyProcess(Process):
  def __init__(self,name,func,args):
    super(MyProcess,self).__init__()
    self.name = name
    self.func = func
    self.args = args
    self.res = ''

  def run(self):
    self.res = self.func(*self.args)
    print self._target
    print self.name
    print self.res,'##'
    return (self.res,'kel')

def func(name):
  print 'start process...'
  return name.upper()

if __name__ == '__main__':
  processes = []
  result = []
  for i in range(3):
    p = MyProcess('process',func,('kel',))
    processes.append(p)
  for i in processes:
    i.start()
  for i in processes:
    i.join()
  for i in processes:
    result.append(i.res)
  for i in result:
    print i