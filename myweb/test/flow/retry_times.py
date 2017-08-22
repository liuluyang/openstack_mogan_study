

from taskflow import task, engines, retry
from taskflow.patterns import linear_flow


class Fir(task.Task):
    def execute(self, *args, **kwargs):
        print 'i am fir class'

class EchoTask(task.Task):
     def execute(self, message):
         print message
         #raise ValueError


flow = linear_flow.Flow('send_message', retry=retry.Times(3)).add(
    Fir(),
    EchoTask(),
    )


engine = engines.load(flow, store={'message':'hello'})
engine.run()



