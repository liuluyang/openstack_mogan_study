#coding:utf8

#列出所有子字符串 然后一次检查找出最长的回文
import time
def checktime(f):

    def fun(*args,**kwargs):
        t = time.clock()
        r = f(*args,**kwargs)
        print time.clock()-t
        return r
    return fun

@checktime
def longest_palindromic(text):
    width = len(text)
    sub_str = []
    for inter in range(2,width+1):
        for i in range(width-inter+1):
            sub_str.append(text[i:i+inter])
    #print sub_str
    result = (0,text[0])
    for s in sub_str:
        if s==s[::-1] and len(s)>result[0]:
            result = (len(s), s)

    return result[-1]

#第二种算法
@checktime
def checkio(text):
    result = (0,text[0])
    width = len(text)
    for inter in range(2,width+1):
        for i in range(width):
            if i+(width+2-inter)<=width:
                s = text[i:i+(width+2-inter)]
                #print s
                if s==s[::-1]:
                    return s
@checktime
def longest_palindromic_2(text):
    for i in range(len(text)+1,0,-1):
        for k in range(len(text)+1-i):
            longest = text[k:k+i]
            if longest == longest[::-1]:
                return longest
    return ''

import itertools

long_text = '''
hffffjahfjkafjdsuhfsufhd
fsdjfwenjnjkcnsfiewfewoi
'''
bit_text = 'ababbac'
print longest_palindromic(long_text)
print longest_palindromic_2(long_text) #fast
print checkio(long_text)
#print longest_palindromic('a')
if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"