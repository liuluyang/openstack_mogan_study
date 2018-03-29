#coding:utf8


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        num_dict = {'1':'abc','2':'def','3':'ghi','4':'jkl','5':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        result = ['']
        for i in digits:
            s = num_dict[i]
            result = sorted(result*len(s))
            print result
            z = zip(result,list(s)*len(result))
            result = [one+two for one,two in z]

        return result

s = Solution()
print s.letterCombinations('234')