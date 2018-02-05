#coding:utf8

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits) == 0:
            digits = [1]
        elif digits[-1] == 9:
            digits = self.plusOne(digits[:-1])
            digits.extend([0])
        else:
            digits[-1] += 1
        return digits

s = Solution()
print s.plusOne([9,9])

def test(nums):
    s = ''.join([str(i) for i in nums])
    print s
    nums = [int(i) for i in str(int(s)+1)]
    print nums

print test([9,9])

