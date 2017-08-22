

from taskflow import engines, task, retry
from taskflow.patterns import linear_flow, unordered_flow
from taskflow.types import failure

class Patter_data(task.Task):

    agr = ['name','size']
    #default_provides = set(['name','size','new'])

    def execute(self,*args, **kwargs):
        print kwargs
        name = 'new'+kwargs['name']
        size = kwargs['size']*10
        print name,size
        print '#'*20

        return {'size':size,'name':name,'new':'nnew'}
    def revert(self, result, *args, **kwargs):
        if isinstance(result, failure.Failure):
            print 'patter_data is failed'
            return None

        print 'patter_data is rollback'

class Start(task.Task):

    agr = ['obj']
    default_provides = set(agr)

    def execute(self, name, size, new, *args, **kwargs):
        obj = '%s is %d'%(name,size)
        print obj
        print new
        print '#'*20
        return {'obj':obj}

    def revert(self, result, *args, **kwargs):
        if isinstance(result, failure.Failure):
            print 'start is failed'
            return None
        print 'start is rollback'

class Finish(task.Task):
    agr = ['done']
    default_provides = set(agr)

    def execute(self, obj, *args, **kwargs):
        done = obj+' is finished'
        print done
        print '#'*20
        raise ValueError('Error')
        #return {'done':done}
    def revert(self, result, *args, **kwargs):
        if isinstance(result, failure.Failure):
            print 'finish is failed'
            print result
            return False

        print 'finish is rollback'


def start_flow(name, data):
    flow_api = linear_flow.Flow(name, retry=retry.AlwaysRevert())
    flow_api.add(
        Patter_data(requires=['name','size'], provides={'name','size','new'}),
        Start(),
        Finish(),
    )

    try:
        engine = engines.load(
            flow_api,
            engine_conf = {'engine':'serial'},
            store = data
        )
        engine.run()
    except:
        print 'workflow is failed'

    data_f = engine.storage.fetch('name')
    print 'that is the fetch data done:'
    print data_f

data = {
    'name':'server',
    'size':10,
    'other':'other data'
}
if __name__ == '__main__':
    start_flow('flowdemo',data)


