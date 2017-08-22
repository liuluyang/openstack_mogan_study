
import logging
import os
import sys


logging.basicConfig(level=logging.ERROR)

top_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                       os.pardir,
                                       os.pardir))

sys.path.insert(0, top_dir)


import taskflow.engines
from taskflow.patterns import graph_flow as gf,linear_flow as lf
#from taskflow.patterns import linear_flow as lf
from taskflow import task
from taskflow.types import notifier
from taskflow.types import notifier

any = notifier.Notifier.ANY

ANY = notifier.Notifier.ANY

import example_utils as eu  # noqa


# INTRO: This example shows how a graph flow and linear flow can be used
# together to execute dependent & non-dependent tasks by going through the
# steps required to build a simplistic car (an assembly line if you will). It
# also shows how raw functions can be wrapped into a task object instead of
# being forced to use the more *heavy* task base class. This is useful in
# scenarios where pre-existing code has functions that you easily want to
# plug-in to taskflow, without requiring a large amount of code changes.


def build_frame():
    print 'build_frame...'
    #return 'steel'
    return {'frame':'steel','error':'err'}


def build_engine():
    print 'build_engine...'
    return 'honda'


def build_doors():
    print 'build_doors...'
    return '2'


def build_wheels():
    print 'build_wheels...'
    return '4'


# These just return true to indiciate success, they would in the real work
# do more than just that.

def install_engine(frame, engine):
    print 'install_engine'
    return True


def install_doors(frame, windows_installed, doors):
    print 'install_doors'
    print doors
    return True


def install_windows(frame, doors):
    print 'install_windows'
    return True


def install_wheels(frame, engine, engine_installed, wheels):
    print 'install_wheels'
    return True


def trash(**kwargs):
    print 'this is trash func'
    eu.print_wrapped("Throwing away pieces of car!")


def startup(spec, **kwargs):
    # If you want to see the rollback function being activated try uncommenting
    # the following line.
    #
    # raise ValueError("Car not verified")
    print spec
    print 'this is startup func'
    return True


def verify(spec, **kwargs):
    # If the car is not what we ordered throw away the car (trigger reversion).
    print 'this is verify func'
    print kwargs
    for key, value in kwargs.items():
        if spec[key] != value:
            raise Exception("Car doesn't match spec!")
    return True


# These two functions connect into the state transition notification emission
# points that the engine outputs, they can be used to log state transitions
# that are occurring, or they can be used to suspend the engine (or perform
# other useful activities).
def flow_watch(state, details):
    print 'detail:',details
    print('Flow => %s' % state)


def task_watch(state, details):
    print 'detail:',details
    print('Task %s => %s' % (details.get('task_name'), state))


flow = lf.Flow("make-auto").add(
    task.FunctorTask(startup, revert=trash, provides='ran'),
    # A graph flow allows automatic dependency based ordering, the ordering
    # is determined by analyzing the symbols required and provided and ordering
    # execution based on a functioning order (if one exists).
    gf.Flow("install-parts").add(
        task.FunctorTask(build_frame, provides={'frame','error'}),
        task.FunctorTask(build_engine, provides='engine'),
        task.FunctorTask(build_doors, provides='doors'),
        task.FunctorTask(build_wheels, provides='wheels'),
        # These *_installed outputs allow for other tasks to depend on certain
        # actions being performed (aka the components were installed), another
        # way to do this is to link() the tasks manually instead of creating
        # an 'artificial' data dependency that accomplishes the same goal the
        # manual linking would result in.
        task.FunctorTask(install_engine, provides='engine_installed'),
        task.FunctorTask(install_doors, provides='doors_installed'),
        task.FunctorTask(install_windows, provides='windows_installed'),
        task.FunctorTask(install_wheels, provides='wheels_installed')),
    task.FunctorTask(verify, requires=['frame',
                                       'engine',
                                       'doors',
                                       'wheels',
                                       'engine_installed',
                                       'doors_installed',
                                       'windows_installed',
                                       'wheels_installed','error']))

# This dictionary will be provided to the tasks as a specification for what
# the tasks should produce, in this example this specification will influence
# what those tasks do and what output they create. Different tasks depend on
# different information from this specification, all of which will be provided
# automatically by the engine to those tasks.
spec = {
    "frame": 'steel',
    "engine": 'honda',
    "doors": '2',
    "wheels": '4',
    # These are used to compare the result product, a car without the pieces
    # installed is not a car after all.
    "engine_installed": True,
    "doors_installed": True,
    "windows_installed": True,
    "wheels_installed": True,
    "error":"err"
}


engine = taskflow.engines.load(flow, store={'spec': spec.copy()})

# This registers all (ANY) state transitions to trigger a call to the
# flow_watch function for flow state transitions, and registers the
# same all (ANY) state transitions for task state transitions.
engine.notifier.register('*', flow_watch)
engine.atom_notifier.register(ANY, task_watch)
#engine.notifier.register("*", flow_watch)

eu.print_wrapped("Building a car")
engine.run()
print engine.storage.fetch('spec')
print engine.storage.fetch_all()

# Alter the specification and ensure that the reverting logic gets triggered
# since the resultant car that will be built by the build_wheels function will
# build a car with 4 doors only (not 5), this will cause the verification
# task to mark the car that is produced as not matching the desired spec.
#spec['doors'] = 5

engine = taskflow.engines.load(flow, store={'spec': spec.copy()})
engine.notifier.register(ANY, flow_watch)
engine.atom_notifier.register(ANY, task_watch)

eu.print_wrapped("Building a wrong car that doesn't match specification")
try:
    engine.run()
except Exception as e:
    eu.print_wrapped("Flow failed: %s" % e)