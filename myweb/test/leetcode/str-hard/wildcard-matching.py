#coding:utf8

import re
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i = 0
        j = 0
        s_l = len(s)
        p_l = len(p)
        start_s = -1
        start_p = -1
        while i<s_l:
            if j<p_l and (s[i]==p[j] or p[j]=='?'):
                i+=1
                j+=1
            elif j<p_l and p[j]=='*':
                start_s = i
                start_p = j
                j+=1
            elif start_p>=0:
                i = start_s+1
                start_s+=1
                j = start_p
            else:
                return False
        #print j
        if len(p[j:])==p[j:].count('*'):
            return True
        else:
            return False






s = Solution()
print s.isMatch('ab','*a')
print s.isMatch('aa','a')
print s.isMatch('aa','*')
print s.isMatch('aaa','???')
print s.isMatch("abefcdgiescdfimde","ab*cd?i*de")

# print re.findall('ab.*cd[a-z]{1}i.*de','abefcddiescdfimdef')
# print re.findall('[a-z]{1}','')

#print re.findall('(ab\w{1}a)(ab\w{1}a)','abwfabhafabha')


