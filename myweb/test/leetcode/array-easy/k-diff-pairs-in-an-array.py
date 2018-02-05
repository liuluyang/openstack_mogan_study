#coding:utf8


from itertools import combinations
from time import clock

def test1():
    start = clock()
    n = 0
    for i,v in combinations(range(10000),2):
        if abs(i-v)==2:
            n+=1
    print clock()-start
    print  n
    #14s 9998

def test2(nums, k):
    start = clock()
    nums = sorted(nums)
    result = set()
    for i,n in enumerate(nums):
        for second in nums[i+1:]:
            if second-n==k:
                result.add(n)
            if second-n>k:
                break
    print clock()-start
    #0.2s 9998
    return len(result)

#print test2(range(10000), 2)

from collections import Counter

from collections import Counter
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k>0:
            return len(set(nums)&set(n+k for n in nums))
        elif k==0:
            return len([v for v in Counter(nums).values() if v>1])
        else:
            return 0

s = Solution()
print s.findPairs([1,2,1,4,5],0)