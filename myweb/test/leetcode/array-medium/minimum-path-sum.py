#coding:utf8


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        [[1,3,1],
        [1,5,1],
        [4,2,1]]
        """
        # m = len(grid)-1
        # n = len(grid[0])-1
        # temp = {}
        # def t(grid,m,n):
        #     if (m,n) in temp:
        #         return temp[(m,n)]
        #     if m==n==0:
        #         return grid[0][0]
        #     if m<0 or n<0:
        #         return 100
        #     val = min(t(grid,m-1,n),t(grid,m,n-1))+grid[m][n]
        #     if (m,n) not in temp:
        #         temp[(m,n)]=val
        #     return val
        # return t(grid,m,n)

        # m = len(grid)
        # n = len(grid[0])
        # result = {(0,0):grid[0][0]}
        # for i in range(m+n-2):
        #     for key,val in result.items():
        #         m_sub = key[0]
        #         n_sub = key[1]
        #         if m_sub+1<m:
        #             if (m_sub+1,n_sub) not in result:
        #                 result[(m_sub+1,n_sub)]=grid[m_sub+1][n_sub]+val
        #             else:
        #                 result[(m_sub + 1, n_sub)] = min(grid[m_sub + 1][n_sub] + val,result[(m_sub + 1, n_sub)])
        #         if n_sub+1<n:
        #             if (m_sub,n_sub+1) not in result:
        #                 result[(m_sub,n_sub+1)]=grid[m_sub][n_sub+1]+val
        #             else:
        #                 result[(m_sub, n_sub + 1)] = min(grid[m_sub][n_sub + 1] + val,result[(m_sub, n_sub + 1)])
        # return result[(m-1,n-1)]

        dp = [0] * len(grid)
        dp[0] = grid[0][0]
        for i in range(1, len(grid)):
            dp[i] = dp[i - 1] + grid[i][0]
        print dp
        for j in range(1, len(grid[0])):
            for i in range(len(grid)):
                dp[i] = min(dp[i], dp[i - 1]) + grid[i][j] if i > 0 else dp[i] + \
                                                                         grid[
                                                                             i][
                                                                             j]
        return dp[len(grid) - 1]


s = Solution()
print s.minPathSum([[1,3,1],
                    [1,5,1],
                    [4,2,1]])