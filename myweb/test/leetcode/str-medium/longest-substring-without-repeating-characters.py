#c0ding:utf8

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # if len(set(s))==len(s):
        #     return len(s)
        # max_l = 0
        # check = []
        # for i in s:
        #     if i not in check:
        #         check.append(i)
        #     else:
        #         l = len(check)
        #         max_l = max(max_l,l)
        #         check = check[check.index(i)+1:]
        #         check.append(i)
        #
        # return max(max_l,len(check))
        check = {}
        start = 0
        max_len = 0
        for index,s in enumerate(s):
            if s in check and check[s]>=start:
                print index-start
                start = check[s]+1
            else:
                max_len = max(max_len, index-start+1)
            check[s] = index
        print start
        return max_len

s = Solution()
print s.lengthOfLongestSubstring("ohvhjdmlj")
