#coding:utf8


class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp = set([])
        result = set([])
        for i in nums:
            if i in temp:
                result.add(i)
            else:
                temp.add(i)
        return list(result)