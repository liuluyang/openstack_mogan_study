#coding:utf8

from itertools import combinations,permutations
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        for i in range(len(nums)+1):
            result.extend(map(list,combinations(nums,i)))
        return result


s = Solution()
print s.subsets(['a','b','c'])