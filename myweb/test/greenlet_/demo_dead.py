from greenlet import greenlet
def test1():
    gr2.switch(1)
    print 'test1 finished'

def test2(x):
    print 'test2 first', x
    z = gr1.switch()
    print 'test2 back', z

gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()
print 'gr1 is dead?: %s, gr2 is dead?: %s' % (gr1.dead, gr2.dead)
#print '#'*10
#gr2.switch(2)
#print 'gr1 is dead?: %s, gr2 is dead?: %s' % (gr1.dead, gr2.dead)
#print gr2.switch(10)