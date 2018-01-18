#coding:utf8

def checkio(one,two):
    one, two = max(one, two),min(one, two)
    one = bin(one).split('b')[-1]
    two = bin(two).split('b')[-1].zfill(len(one))
    result = 0
    for k,y in zip(one,two):
        if k!=y:
            result+=1
    return result

#print checkio(117,17)

print checkio(117, 17) == 3
print checkio(1, 2) == 2
print checkio(16, 15) == 5