from itertools import groupby
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i,v in groupby(nums):
            n = len(list(v))
            if i==1 and n>result:
                result = n

        return result


s = Solution()
print s.findMaxConsecutiveOnes([1,1,0,1])