#coding:utf8


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum=big=small=nums[0]
        for n in nums[1:]:
            big, small=max(n, n*big, n*small), min(n, n*big, n*small)
            maximum=max(maximum, big)
        return maximum





s = Solution()
print s.maxProduct([1,2,0,-1,-3,0,5,])

print s.maxProduct([1,2,3,4,5])

print s.maxProduct([-1,-2,-3,-2])