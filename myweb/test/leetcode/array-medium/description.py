#coding:utf8

from itertools import combinations,permutations

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # result = []
        # for i in range(len(nums)+1):
        #     #print permutations(nums,i)
        #     result+=[list(z) for z in permutations(nums,i)]
        # print result
        # return result

        power_set = [[]]
        for num in sorted(nums):
            power_set += [item + [num] for item in power_set]
            print power_set
        return power_set


s = Solution()
print s.subsets([1,2,3])