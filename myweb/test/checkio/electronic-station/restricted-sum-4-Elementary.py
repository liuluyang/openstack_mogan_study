#coding:utf8

def checkio(data):
    if not data:
        return 0
    else:
        return data.pop()+checkio(data)

print checkio([1,2,3])
print checkio([2,3,4,5,6,7,8,9,])