#coding:utf8


class Stu(object):
        _num = 0
        def __init__(self):
            Stu._num +=1

def t():

    s1 = Stu()
    print s1._num
    #s2 = Stu()
#print s2._num

t()
t()

print u'斯蒂芬'


def generator_t():
    print ('start')
    yield 1

def normal_():
    return 1

print (generator_t(), type(generator_t()))
print (normal_(), type(normal_()))

t = generator_t()
print (t.next())
#print (next(t))