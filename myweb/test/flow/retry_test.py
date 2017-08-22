

from taskflow import task, engines, retry
from taskflow.patterns import linear_flow

class EchoTask(task.Task):
     def execute(self, *args, **kwargs):
         print(self.name)
         print(args)
         print(kwargs)
         if kwargs:
             if kwargs.get('value')=='c':
                 print 'this is right'
             else:
                 raise ValueError('error')

flow = linear_flow.Flow('f1').add(
     EchoTask('t1'),
    linear_flow.Flow('f2', retry=retry.ForEach(values=['a', 'b', 'c'], name='r1', provides='value')).add(
         EchoTask('t2'),
         EchoTask('t3', requires='value')),
     EchoTask('t4'))

engine = engines.load(flow)
engine.run()