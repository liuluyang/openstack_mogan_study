#coding:utf8

from itertools  import combinations
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        for i in range(len(nums)+1):
            for tup in combinations(nums, i):
                tup = sorted(list(tup))
                if tup not in results:
                    results.append(tup)
        return results

s = Solution()
print s.subsetsWithDup([4,4,4,1,4])