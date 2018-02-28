#coding:utf8



class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.insert(0,nums[0])
        nums.append(nums[-1])
        for index,num in enumerate(nums[1:-1]):
            if num>=nums[index]:
                #print num
                if num>=nums[index+2]:
                    return index


s = Solution()
print s.findPeakElement([1,2,3,1])
print s.findPeakElement([1,2])