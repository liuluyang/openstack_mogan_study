#coding:utf8


class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        length = len(s)
        s = list(s)
        for i in range(0,length/k+1,2):
            print i
            s[i*k:i*k+k]=s[i*k:i*k+k][::-1]
        print s
        return ''.join(s)

s = Solution()
print s.reverseStr('abcdefg',2)
