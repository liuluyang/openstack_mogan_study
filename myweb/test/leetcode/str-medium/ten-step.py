#coding:utf8

from itertools import combinations,permutations
def test():
    check = [[]]
    result = []
    while check:
        tmp = check.pop(0)
        for i in range(1,3):
            if sum(tmp)+i==20:
                result.append(tmp+[i])
            elif sum(tmp)+i<20:
                check.append(tmp+[i])
            else:
                break
    # for i in result:
    #     print i
    return len(result)
    pass

#print test()  #<=20

#print len(list(permutations([1,1,2,2,2,2],2)))

def test_2(n):
    if n==1:
        return 1
    if n==2:
        return 2
    return test_2(n-2)+test_2(n-1)

#print test_2(20) #<=30

def test_3(n):
    count = 0
    check = [0]
    while check:
        now = check.pop(0)
        for i in range(1,3):
            temp = now+i
            if temp<n:
                check.append(temp)
            elif temp==n:
                count+=1
    return count

#print test_3(20)  #<=20

def test_4(n):
    if n==1:
        return 1
    if n==2:
        return 2
    v = test_2(n-2)+test_2(n-1)
    print n,v
    return v

#print test_4(4)

def test_5(n):
    a = 1
    b = 2
    for i in range(n-2):
        a,b = b,a+b

    return b

print test_5(6)

