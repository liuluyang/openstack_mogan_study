#coding:utf8


class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_dict = {}
        for i,num in enumerate(nums):
            if num in nums_dict:
                nums_dict[num].append(i)
            else:
                nums_dict[num]=[i]
        print nums_dict
        m,n = 0,0
        for v in nums_dict.values():
            _len = len(v)
            result = v[-1]-v[0]
            if _len>m:
                m = _len
                n = result
            if _len==m and result<n:
                n = result
        return n+1



s = Solution()
print s.findShortestSubArray([1,2,2,1,3])