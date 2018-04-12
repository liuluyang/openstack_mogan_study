#coding:utf8

import copy
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        result = copy.deepcopy(board)
        def check(board,num,x,y):
            count = 0
            temp = [(-1,-1),(+1,+1),(-1,+1),(+1,-1),(0,+1),(0,-1),(+1,0),(-1,0)]
            for i,j in temp:
                if x+i>=0 and y+j>=0:
                    try:
                        count+=board[x+i][y+j]
                    except:
                        pass
            if num==1:
                if count==2 or count==3:
                    return 1
                else:
                    return 0
            else:
                if count==3:
                    return 1
                else:
                    return 0
        for i,nums in enumerate(board):
            for j,num in enumerate(nums):
                result[i][j]=check(board,num,i,j)
        return result


s = Solution()
print s.gameOfLife([[1]])