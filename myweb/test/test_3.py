
def test():
    return 1,2,3

d,f,g = test()

print d,f,g

from myweb.test import olso_log_test

olso_log_test.test()


num = 2
data = [1,2]
def _anti(num, data):
    def retry(num, data):
        new_data = data[0]
        data.pop(0)
        new_num = num+1
        print new_data,'new_data'
        print new_num,'new_num'
        #print len(data)
        if len(data)==1:
            print 'len'
            return data
        print 'binhd'


    for i in range(2):
        re = retry(num, data)
        print re,'[]'
        print num
        print data
        return 111
d = _anti(num, data)
if d == 111:
    print 'ok'

def t():
    for i in [1,2,3]:
        for j in [4,5,6]:
            if j in [4]:
                return j
        #raise IOError('d')
t = t()
if t:
    print t



