#coding:utf8

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = ['(']
        for i in range(1, n * 2):
            length = len(result)
            for j in range(length):
                s = result.pop(0)
                num = s.count('(')
                if 0 <= num * 2 - i + 1 <= n and num < n:
                    result.append(s + '(')
                if 0 <= num * 2 - i - 1:
                    result.append(s + ')')
            # result = result[length:]
        return [i for i in result if i[-1] != '(']
s = Solution()
print s.generateParenthesis(3)