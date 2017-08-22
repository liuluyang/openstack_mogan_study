import logging
import os
import sys

logging.basicConfig(level=logging.DEBUG)

top_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                       os.pardir,
                                       os.pardir))
sys.path.insert(0, top_dir)

from taskflow import engines
from taskflow.patterns import linear_flow
from taskflow import task
from taskflow.listeners import logging as logging_listener
# INTRO: This example shows how a task (in a linear/serial workflow) can
# produce an output that can be then consumed/used by a downstream task.


class TaskA(task.Task):
    #default_provides = {'df','fg'}

    def execute(self,df, lis, **kwargs):
        print kwargs
        print("Executing '%s'" % (self.name))
        #return {'df':'s','fg':'ss'}
        #kwargs.get('server')['id']=2
        print df
        lis.pop(0)
        return {'df':11,'kk':22}



class TaskB(task.Task):
    def execute(self, df, fg, server, kk, lis, **kwargs):
        print("Executing '%s'" % (self.name))
        print("Got input '%s,%s'" % (df, fg ))
        #print k
        print server
        print kwargs
        print kk
        print lis



print("Constructing...")
wf = linear_flow.Flow("pass-from-to")
wf.add(TaskA('taska', provides={'df','kk'}), TaskB('taskb', ))

print("Loading...")
e = engines.load(wf, store={"name":"hello","df":123,"fg":"f","server":{"id":1},"lis":[1,2]})

print("Compiling...")
e.compile()

print("Preparing...")
e.prepare()

print("Running...")
with logging_listener.DynamicLoggingListener(e):
    e.run()

print("Done...")