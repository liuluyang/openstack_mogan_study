#coding:utf8

import re
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for i in  s.split(' '):
            if i:
                result+=1
        rr = re.compile(r'(\S+)')
        print rr.findall(s)
        print s.split()
        return result

s = Solution()
print s.countSegments('sfs   fs, dsf')