#coding:utf8

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)
        for i in range(length/2):
            if length%(i+1)==0 and s[:i+1]*(length/(i+1))==s:
                return True

        return False

s = Solution()
print s.repeatedSubstringPattern('aa')
