#coding:utf8

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #if sorted(nums)[-1]<=0:
            #return max(nums)
        results=max(nums)
        nums_sum = 0
        for i in nums:
            nums_sum+=i
            #if i>0:
            if nums_sum<0:
                nums_sum = 0
                #print nums_sum
            #results.add(nums_sum)
            if nums_sum>results:
                results = nums_sum
        #print nums_sum
        #print results
        #results.add(nums_sum)
        return results

s = Solution()
print s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print s.maxSubArray([-2,1,0,-3])