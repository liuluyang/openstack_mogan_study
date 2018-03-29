#coding:utf8


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        check = {0: -1}
        max_length = 0
        count = 0
        for index, sign in enumerate(s):
            if sign == '(':
                count += 1
                check[count] = index
            else:
                count -= 1
                if count in check:
                    max_length = max(max_length, index - check[count])
                else:
                    count = 0
                    check = {0: index}
        return max_length


s = Solution()
#print s.longestValidParentheses("(()((())")
#print s.longestValidParentheses('()((())')
print s.longestValidParentheses(")()())()()(")