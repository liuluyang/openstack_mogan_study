#coding:utf8


class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.insert(0,0)
        n = 0
        for i in range(1,len(nums)-1):
            if nums[i]>nums[i+1]:
                if n>0:
                    return False
                n+=1
                if nums[i-1]>nums[i+1]:
                    nums[i+1]=nums[i]

        return True

s = Solution()
print s.checkPossibility([3,4,2,5])
print s.checkPossibility([4,2,3])
print s.checkPossibility([2,4,1,3])