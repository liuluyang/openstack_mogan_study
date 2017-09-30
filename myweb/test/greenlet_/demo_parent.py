import greenlet

#switch not call

def test1(x, y):
    print id(greenlet.getcurrent()), id(greenlet.getcurrent().parent) # 40240272 40239952
    z = gr2.switch(x+y)
    print 'back z', z

def test2(u):
    print 'test2'
    print id(greenlet.getcurrent()), id(greenlet.getcurrent().parent) # 40240352 40239952
    #gr1.switch('wo')
    #return u
    #return 1

gr1 = greenlet.greenlet(test1)
gr2 = greenlet.greenlet(test2)
print id(greenlet.getcurrent()), id(gr1), id(gr2)     # 40239952, 40240272, 40240352
#print gr1.switch("hello", " world"), 'back to main'    # hehe back to main

print '#'*10
print test1('h', 'w')