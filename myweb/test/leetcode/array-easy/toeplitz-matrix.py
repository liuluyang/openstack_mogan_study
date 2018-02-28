#coding:utf8
import numpy as np
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        nums = np.array(matrix)
        print nums
        m,n = nums.shape
        print m,n
        num_new = np.rot90(nums, 2)
        print num_new

        positions = [(0,i) for i in range(n)]+[(i,0) for i in range(1,m)]

        print positions

        for posi in positions:
            x = posi[0]
            y = posi[1]
            check = matrix[x][y]
            print check
            for i in range(1,m):
                try:
                    x+=1
                    y+=1
                    print matrix[x][y]
                    if check!=matrix[x][y]:
                        return False
                except:
                    break

        return True





s = Solution()
#print s.isToeplitzMatrix([[1,2],[2,1],[3,2]])

#print s.isToeplitzMatrix([[36,59,71,15,26,82,87],[56,36,59,71,15,26,82],[15,0,36,59,71,15,26]])

print s.isToeplitzMatrix([[44,35,39],[15,44,35],[17,15,44],[80,17,15],[43,80,0],[77,43,80]])
