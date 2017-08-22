import logging
import os
import random
import sys
import time

logging.basicConfig(level=logging.ERROR)

top_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                       os.pardir,
                                       os.pardir))
sys.path.insert(0, top_dir)

from taskflow import engines
from taskflow.listeners import timing
from taskflow.patterns import linear_flow as lf
from taskflow import task

# INTRO: in this example we will attach a listener to an engine
# and have variable run time tasks run and show how the listener will print
# out how long those tasks took (when they started and when they finished).
#
# This shows how timing metrics can be gathered (or attached onto an engine)
# after a workflow has been constructed, making it easy to gather metrics
# dynamically for situations where this kind of information is applicable (or
# even adding this information on at a later point in the future when your
# application starts to slow down).


class VariableTask(task.Task):
    def __init__(self, name):
        super(VariableTask, self).__init__(name)
        self._sleepy_time = random.random()

    def execute(self):
        time.sleep(self._sleepy_time)


f = lf.Flow('root')
f.add(VariableTask('a'), VariableTask('b'), VariableTask('c'))
e = engines.load(f)
with timing.PrintingDurationListener(e):
    e.run()