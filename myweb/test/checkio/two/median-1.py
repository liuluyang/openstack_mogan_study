#coding:utf8
from itertools import groupby
'''
中位数
'''
def checkio(data):

    #replace this for solution
    data.sort()
    _len = len(data)
    print _len,type(_len)
    if _len%2 == 0:
        print _len/2
        n = (data[_len/2]+data[_len/2-1])/2
    else:
        print (_len-1)/2,type((_len-1)/2)
        n = data[(_len-1)/2]


    return n

print checkio([1,2,3])


