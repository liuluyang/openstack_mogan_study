


def _make_property(cla):

    if cla.name:
        n = cla.name
        def setter(self, val, n, field):
            print 'setter func'
        print 'if name'
        setattr(cla, cla.name, property(setter))

    return cla


@_make_property
class Test(object):

    name = 'Test'

t = Test()
print t.name
setattr(t, 'name', 'myname')
print t.name

