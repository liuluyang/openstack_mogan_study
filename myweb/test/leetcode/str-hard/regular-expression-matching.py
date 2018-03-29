#coding:utf8

import re
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        #print re.findall(p,s)
        r = re.findall(p, s)
        return True if r and r[0] == s else False


s = Solution()
print s.isMatch('ab','a')