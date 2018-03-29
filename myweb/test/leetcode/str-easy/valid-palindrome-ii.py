#coding:utf8




class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = list(s)
        l = 0
        r = len(s)-1
        while l<r:
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                s1,s2 = s[l+1:r+1],s[l:r]
                return self.check(s1) or self.check(s2)
        return True
    def check(self, ss):
        left = 0
        right = len(ss)-1
        while left<right:
            if ss[left]==ss[right]:
                left+=1
                right-=1
            else:
                return False
        return True

s = Solution()
print s.validPalindrome('abga')



