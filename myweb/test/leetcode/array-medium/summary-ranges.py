#coding:utf8


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        result = []
        start = end = nums[0]
        for index in xrange(1,len(nums)):
            if nums[index]==nums[index-1]+1:
                end +=1
            else:
                if start==end:
                    result.append(str(start))
                else:
                    result.append(str(start)+'->'+str(end))
                start = end = nums[index]
        if start == end:
            result.append(str(start))
        else:
            result.append(str(start) + '->' + str(end))
        return result


s = Solution()
print s.summaryRanges([0,1,3,5,6,7])
