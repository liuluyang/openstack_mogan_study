#coding:utf8

from itertools import groupby
import string
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # a = []
        # b = []
        # for i in s:
        #     if i not in a:
        #         a.append(i)
        #     else:
        #         b.append(i)
        # for i in a:
        #     if i not in b:
        #         return s.find(i)
        # return -1
        
        minIndex = 100000
        for i in string.ascii_lowercase:
            curIndex = s.find(i)
            if curIndex!=-1 and curIndex==s.rfind(i):
                minIndex = min(minIndex,curIndex)
        return minIndex if minIndex!=100000 else -1

s = Solution()
print s.firstUniqChar('loveleetcode')