#coding:utf8

import numpy as np
import copy
def test(M,position,m,n):
    a,b = position
    around = [
            (a,b+1),(a,b-1),
            (a+1,b),(a-1,b),
            (a+1,b+1),(a-1,b-1),
            (a+1,b-1),(a-1,b+1)
        ]
    result = M[a][b]
    nums = 1
    #print m,n
    for x,y in around:
        if 0<=x<=m and 0<=y<=n:
            result+=M[x][y]
            #print m[x][y]
            nums+=1

    return result/nums


class Solution(object):
    def imageSmoother(self, M):
        nums = copy.deepcopy(M)
        m,n = len(M),len(M[0])
        m,n = m-1,n-1
        for i,x in enumerate(nums):
            for ii,y in enumerate(x):
                M[i][ii]=test(nums,(i,ii),m,n)
        #return test(M,(0,0))
        return M


s = Solution()
# print s.imageSmoother([
#     [1,2,3,4],
#     [4,5,6,7],
#     [1,2,1,3]
# ])

# print s.imageSmoother(
#         [[2,3,4],
#          [5,6,7],
#          [8,9,10],
#          [11,12,13],
#          [14,15,16]]
# )

print s.imageSmoother([[1,1,1],[1,0,1],[1,1,1]])