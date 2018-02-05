#coding:utf8

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = [i for i,v in enumerate(zip(nums,sorted(nums))) if v[0]!=v[1]]
        return result[-1]-result[0]+1 if result else 0


s = Solution()
print s.findUnsortedSubarray([1,2,5,3,4])