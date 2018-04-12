#coding:utf8


class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        if k==1:
            return range(1,n+1)
        nums = range(1,n+1)
        result = []
        last = True
        index = 0
        for i in xrange(k):
            if last:
                result.append(nums.pop())
                last = False
            else:
                result.append(nums[index])
                index+=1
                last = True
        if nums[index]>result[-1]:
            return result+nums[index:]
        return result+nums[index:][::-1]

s = Solution()
print s.constructArray(10,3)