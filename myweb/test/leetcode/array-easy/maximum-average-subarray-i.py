#coding:utf8

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if len(nums)==1:
            return nums[0]
        if k==1:
            return max(nums)
        result = [sum(nums[i:i+k]) for i in range(len(nums))][:-(k-1)]
        print result
        return max(result)/float(k)


s = Solution()
print s.findMaxAverage([1,12,-5,-6,50,3],4)
print s.findMaxAverage([5],1)