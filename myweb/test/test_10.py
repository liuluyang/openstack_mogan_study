


class A(object):
    def __a(self):
        print 'I am A'
    def a(self):
        self.__a()

class B(A):
    def __a(self):
        print 'I am B'
    #def a(self):
        #self.__a()

#a = A()
#a.a()
b = B()
b.a()