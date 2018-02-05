#coding:utf8


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for i in range(len(nums)):
            if val in nums:
                nums.remove(val)
        return len(nums)


s = Solution()
print s.removeElement([3,2,2,3],3)