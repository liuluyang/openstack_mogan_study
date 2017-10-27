
class C(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def m1(self):
        print self.x
        print 'C.m is here'

class D(C):
    def __init__(self, x):
        self.x = x
        pass
    def m(self):
        #super().m()
        print 'D.m is here'

d = D(2)
print d.m1()