#coding:utf8

def checkio(number):

    n = 1
    for i in str(number):
        if i!='0':
            n *=int(i)
    return n