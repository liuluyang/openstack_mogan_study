#coding:utf8


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # if not strs:
        #     return ""
        # common = strs[0]
        # for str in strs[1:]:
        #     if not common:
        #         return ""
        #     for i in range(len(common)):
        #         ii = i+1
        #         if common[0:ii]!=str[0:ii]:
        #             common = common[0:i]
        #             break
        # return common


s = Solution()
print s.longestCommonPrefix(['leets','leetd','lee'])
print s.longestCommonPrefix(['a','b'])
