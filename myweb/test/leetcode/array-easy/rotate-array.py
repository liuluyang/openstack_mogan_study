#coding:utf8


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        double_nums = nums+nums
        n = len(nums)
        i = k%n
        nums[:n] = double_nums[n-i:2*n-i]
