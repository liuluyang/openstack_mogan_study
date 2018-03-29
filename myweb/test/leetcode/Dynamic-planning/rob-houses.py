#coding:utf8


import random
# class Solution(object):
#     def search(self, i, nums):
#         if i < 0:  # 没有商家了，我们要开始销赃
#             return 0
#         #print 1
#         #print i
#         return max(self.search(i - 1, nums), nums[i] + self.search(i - 2, nums))
#
#     def rob(self, nums):
#         return self.search(len(nums) - 1, nums)

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.search(len(nums) - 1, nums, [-1 for i in range(len(nums))])
    def search(self, i, nums, memo):
        if i < 0:
            print '*************'
            return 0
        print i, memo
        if memo[i] != -1:
            print i,'%%%%%%%%%%%'
            return memo[i]
        memo[i] = max(self.search(i - 1, nums, memo), nums[i] + self.search(i - 2, nums, memo))
        print memo,'&&&&&&&&&&'
        return memo[i]


s = Solution()
print s.rob([2,3,1,2,4,1])

nums = [random.randint(0,9) for i in xrange(40)]
#print nums
#print s.rob(nums)
#print random.randint(0,9)