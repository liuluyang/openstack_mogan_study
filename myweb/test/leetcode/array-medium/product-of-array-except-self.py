#coding:utf8

import math
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def product(nums):
            p = 1
            for i in nums:
                p*=i
            return p
        zero = nums.count(0)
        result = [0]*len(nums)
        if zero==1:
            index = nums.index(0)
            nums.remove(0)
            result[index]=product(nums)
        if zero==0:
            p = product(nums)
            for index,i in enumerate(nums):
                result[index]=p/i
        return result





s = Solution()
print s.productExceptSelf([10,10,1])