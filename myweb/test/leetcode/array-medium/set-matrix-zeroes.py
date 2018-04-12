#coding:utf8


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        check = set([])
        for x in range(m):
            is_change = False
            for y in range(n):
                if matrix[x][y] == 0:
                    is_change = True
                    if y not in check:
                        for i in range(x, -1, -1):
                            matrix[i][y] = 0
                        check.add(y)
                else:
                    if y in check:
                        matrix[x][y] = 0
            if is_change:
                matrix[x] = [0] * n