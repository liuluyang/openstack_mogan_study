#coding:utf8


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        #if len(triangle)==1:
            #return triangle[0][0]
        below = triangle[-1]
        for i in range(len(triangle)-2,-1,-1):
            curr = triangle[i]
            for j in range(len(curr)):
                curr[j] += min(below[j], below[j+1])
            below = curr
        return below[0]

s = Solution()
print s.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
])

print s.minimumTotal([[-10]])
#
# print s.minimumTotal([
#     [-1],
#     [2,3],
#     [1,-1,-3]
# ])

