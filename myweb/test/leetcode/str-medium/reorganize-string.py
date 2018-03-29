#coding:utf8

from itertools import groupby
import string
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        length = len(S)
        s = {}
        for i in S:
            if i in s:
                s[i].append(i)
            else:
                s[i]=[i]
        s = sorted(s.values(), key=len, reverse=True)
        print s
        result = s.pop(0)
        if len(result)>length/2+length%2:
            return ''
        s_new = []
        for i in s:
            s_new+=i
        print s_new
        while s_new:
            length = len(result)
            for n in range(1,length*2,2):
                result.insert(n,s_new.pop(0))
                if not s_new:
                    break
        return ''.join(result)






s = Solution()
print s.reorganizeString('wwaaaaaaabbbcc')