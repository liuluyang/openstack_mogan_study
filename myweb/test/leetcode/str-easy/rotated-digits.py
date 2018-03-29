#coding:utf8


class Solution(object):
    def rotatedDigits(self, N):
        ans = 0
        # For each x in [1, N], check whether it's good
        for x in xrange(1, N+1):
            S = str(x)
            # Each x has only rotateable digits, and one of them
            # rotates to a different digit
            if (all(d not in '347' for d in S)
                    and any(d in '2569' for d in S)):
                print x
                ans+=1
        return ans

s = Solution()
print s.rotatedDigits(20)