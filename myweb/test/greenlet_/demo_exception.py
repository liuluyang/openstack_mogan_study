import greenlet
def test1(x, y):
    try:
        z = gr2.switch(x+y)
    except Exception:
        #print 'catch Exception in test1'
        pass

def test2(u):
    assert False,'error'

gr1 = greenlet.greenlet(test1)
gr2 = greenlet.greenlet(test2)
try:
    gr1.switch("hello", " world")
except Exception as e:
    print e
    print 'catch Exception in main'