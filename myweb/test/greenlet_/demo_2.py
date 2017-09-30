import greenlet
def test1(x, y):
    z = gr2.switch(x+y)
    print('test1 ', z)

def test2(u):
    print('test2 ', u)
    gr1.switch(10)

gr1 = greenlet.greenlet(test1)
gr2 = greenlet.greenlet(test2)
gr1.switch("hello", " world")   #('test2 ', 'hello world') ('test1 ', 10)