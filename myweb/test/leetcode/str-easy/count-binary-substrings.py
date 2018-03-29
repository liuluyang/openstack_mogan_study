#coding:utf8


class Solution(object):
    def countBinarySubstrings(self, s):
        groups = [1]
        for i in xrange(1, len(s)):
            if s[i-1] != s[i]:
                groups.append(1)
            else:
                groups[-1] += 1
        print groups
        ans = 0
        for i in xrange(1, len(groups)):
            ans += min(groups[i-1], groups[i])
        return ans

s = Solution()
print s.countBinarySubstrings('00110011')
