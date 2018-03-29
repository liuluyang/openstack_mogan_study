#coding:utf8


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        result = 0
        for index in xrange(length):
            first = index-1
            last = index+1
            while first>=0 and last<length:
                if s[first]==s[last]:
                    result+=1
                    first-=1
                    last+=1
                else:
                    break
            first = index
            last = index+1
            while first>=0 and last<length:
                if s[first]==s[last]:
                    result+=1
                    first-=1
                    last+=1
                else:
                    break

        return result+length

s = Solution()
print s.countSubstrings('aabcbe')