#coding:utf8


class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count = 0
        max_num = 0
        index = -1
        for num in arr:
            max_num = max(max_num,num)
            index+=1
            if index==max_num:
                count+=1
        return count

s = Solution()
print s.maxChunksToSorted([1,0,2,3,4])
print s.maxChunksToSorted([4,3,2,1,0])
