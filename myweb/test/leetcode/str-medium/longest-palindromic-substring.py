#coding:utf8


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        size = len(s)
        if size <= 1 or s == s[::-1]:
            return s
        start, maxlen = 0, 1
        for idx in range(1, size):
            add2 = s[idx - maxlen - 1: idx + 1]
            print add2
            if idx - maxlen - 1 >= 0 and add2 == add2[::-1]:
                start = idx - maxlen - 1
                maxlen += 2
                continue
            add1 = s[idx - maxlen: idx + 1]
            if add1 == add1[::-1]:
                start = idx - maxlen
                maxlen += 1
        return s[start: (start + maxlen)]


s = Solution()
print s.longestPalindrome('abacdf')
