#coding:utf8

from itertools import groupby,combinations,permutations
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print list(combinations([1,2,2],0))
        for i in groupby(nums):
            print len(list(i[1]))
        other_nums = []
        for index in range(1,len(nums)-1):
            if nums[index-1]==nums[index]==nums[index+1]:
                other_nums.append(nums[index])
        if nums:
            for i in other_nums:
                nums.remove(i)
        print nums
        return len(nums)


s = Solution()
print s.removeDuplicates([1,1,1,1,2])