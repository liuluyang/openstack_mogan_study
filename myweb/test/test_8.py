

class Person(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Person:%s'%(self.name)

    def __repr__(self):
        return 'default'

class Stu(Person):
    def __init__(self, name, age):
        super(Stu, self).__init__(name)
        self.age = age

P = Person('xiaoli')
S = Stu('XIao',12)
print P
print S
#this is pull by liu-c
#
