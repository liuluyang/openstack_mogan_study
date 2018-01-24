#coding:utf8
import math
def checkio(x,y,z):
    L = [x,y,z]
    for i in range(3):
        n = L.pop(i)
        if n>=sum(L):
            return [0,0,0]
        L = [x,y,z]

    cosz = float(x**2+y**2-z**2)/(2*x*y)
    cosx = float(z**2+y**2-x**2)/(2*z*y)
    cosy = float(z**2+x**2-y**2)/(2*z*x)
    # print 'cosz',cosz
    # print 'cosx',r2
    # print '弧度',math.acos(r2)
    # print '角度',math.degrees(math.acos(r2))
    L = [
        int(round(math.degrees(math.acos(cosz)))),
        int(round(math.degrees(math.acos(cosx)))),
        int(round(math.degrees(math.acos(cosy))))
    ]
    return sorted(L)


print checkio(3,4,5)
print checkio(1,2,3)