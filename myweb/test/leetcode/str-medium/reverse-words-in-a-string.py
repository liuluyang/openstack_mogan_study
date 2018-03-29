#coding:utf8


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(s.split()[::-1])


s = Solution()
print s.reverseWords("   one.   +two three?   ~four   !five- ")