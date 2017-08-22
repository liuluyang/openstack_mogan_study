


class Values(object):

    dict_ = {1:'dd',2:'gg'}

    def as_dict(self):
        return {'4':'ddd'}

dict_ = {1:'dd',2:'gg'}
va = Values()

def test(**kw):
    print kw

test(**va.as_dict())

_D = 1
def print_d(val):
    print val

class DD(object):


    def dd(self):
        print_d(_D)

d = DD()
d.dd()



