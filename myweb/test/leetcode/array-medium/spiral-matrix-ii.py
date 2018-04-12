#coding:utf8


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        for i in xrange(n):
            result.append([0]*n)
        #print result
        x=y=0
        n = n*n
        num = 1
        def t1(x,y,result,num,n):
            while True:
                #print result
                if num>n:
                    return x,y,result,num,n
                try:
                    if result[x][y]==0:
                        result[x][y]=num
                        #print result,'result',x,y
                    else:
                        return x+1,y-1,result,num,n
                except:
                    return x + 1, y-1, result, num, n
                y+=1
                num+=1
        def t2(x,y,result,num,n):
            while True:
                #print result
                if num>n:
                    return x,y,result,num,n
                try:
                    if result[x][y]==0:
                        result[x][y]=num
                        #print result,'result',x,y
                    else:
                        return x-1,y-1,result,num,n
                except:
                    return x - 1, y-1, result, num, n
                x+=1
                num+=1
        def t3(x,y,result,num,n):
            while True:
                #print result
                if num>n:
                    return x,y,result,num,n
                try:
                    if result[x][y]==0:
                        result[x][y]=num
                        #print result,'result',x,y
                    else:
                        return x-1,y+1,result,num,n
                except:
                    return x-1, y+1, result, num, n
                y-=1
                num+=1
        def t4(x,y,result,num,n):
            while True:
                #print result
                if num>n:
                    return x,y,result,num,n
                try:
                    if result[x][y]==0:
                        result[x][y]=num
                        #print result,'result',x,y
                    else:
                        return x+1,y+1,result,num,n
                except:
                    return x+1, y+1, result, num, n
                x-=1
                num+=1

        # print t1(x,y,result,num,n)
        # print t2(1, 2, [[1, 2, 3], [0, 0, 0], [0, 0, 0]], 4, 9)
        # print t3(2, 1, [[1, 2, 3], [0, 0, 4], [0, 0, 5]], 6, 9)
        # print t4(1, 0, [[1, 2, 3], [0, 0, 4], [7, 6, 5]], 8, 9)
        # print t1(1, 1, [[1, 2, 3], [8, 0, 4], [7, 6, 5]], 9, 9)
        for i in xrange(n):
            x,y,result,num,n = t1(x,y,result,num,n)
            x, y, result, num, n = t2(x, y, result, num, n)
            x, y, result, num, n = t3(x, y, result, num, n)
            x, y, result, num, n = t4(x, y, result, num, n)
            if num>n:
                return result




s = Solution()
print s.generateMatrix(6)

# l = [[0,0,0],[0,0,0],[0,0,0]]
# l[0][0]=1
# print l

l = [[1, 2, 3, 4, 5, 6],
 [20, 21, 22, 23, 24, 7],
 [19, 32, 33, 34, 25, 8],
 [18, 31, 36, 35, 26, 9],
 [17, 30, 29, 28, 27, 10],
 [16, 15, 14, 13, 12, 11]]