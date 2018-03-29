#coding:utf8

from copy import deepcopy

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = list(s)
        a = 'aeiou'
        result = ''
        length = len(s)
        i = 0
        j = length-1
        while j>=0 or i<length:
            #print 'f',j

            while j>=0 and s[j] not in a:
                j-=1
                #print j
            while i<length and s[i] not in a:

                result+=s[i]
                i += 1
                #print result,11
            if j>=0:
                s_list[i]=s[j]
                #print result
            j-=1
            i+=1
        return ''.join(s_list)

s = Solution()
print s.reverseVowels('hello')

print s.reverseVowels('a.')

