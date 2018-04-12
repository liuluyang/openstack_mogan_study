#coding:utf8

from itertools import combinations,permutations
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # temp = [(0,0)]
        # count = 0
        # while temp:
        #     temp2 = []
        #     for t in temp:
        #         new1 = (t[0]+1,t[1])
        #         #print new1
        #         if new1[0]<=m:
        #             if new1==(m-1,n-2) or new1==(m-2,n-1):
        #                 count+=1
        #             else:
        #                 temp2.append(new1)
        #         new2 = (t[0],t[1]+1)
        #         #print new2
        #         if new2[1]<=n:
        #             if new2==(m-1,n-2) or new2==(m-2,n-1):
        #                 count+=1
        #             else:
        #                 temp2.append(new2)
        #     temp = temp2
        # return count

        # def t(x,y,temp):
        #     if x<0 or y<0:
        #         return 0
        #     if (x,y) in temp:
        #         return temp[(x,y)]
        #     if (x,y)==(0,1) or (x,y)==(1,0):
        #         return 1
        #     v = t(x-1,y,temp)+t(x,y-1,temp)
        #     temp[(x,y)]=v
        #     return v
        # return t(m-1,n-1,{})

        # temp = [[1 for j in range(n)] for i in range(m)]
        # print temp
        # for i in range(1,m):
        #     for j in range(1,n):
        #         temp[i][j]=temp[i-1][j]+temp[i][j-1]
        # return temp[-1][-1]

        start = [1]*n
        for i in xrange(m-1):
            temp = [1]*n
            for j in xrange(1,n):
                temp[j]=start[j]+temp[j-1]
            start = temp
        return start[-1]





print len(list(permutations([1,1,2],3)))

s = Solution()
print s.uniquePaths(3,7)
print s.uniquePaths(1,1)
