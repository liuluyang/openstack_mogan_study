#coding:utf8

import numpy as np
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # for i, nums in enumerate(np.rot90(np.array(matrix), 3)):
        #     for j, num in enumerate(nums):
        #         matrix[i][j] = num
        # return matrix
        result = []
        for i in range(len(matrix[0])):
            l = []
            for j in range(len(matrix)-1,-1,-1):
                l.append(matrix[j][i])
            result.append(l)
        return result


s = Solution()
print s.rotate([[1,2],[3,4]])
