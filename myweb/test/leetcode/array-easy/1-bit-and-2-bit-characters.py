#coding:utf8


class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        r = True
        for i,num in enumerate(bits):
            if num==0:
                r = True
            else:
                bits.pop(i)
                r = False

        return r

s = Solution()
print s.isOneBitCharacter([1,1,1,0,0])