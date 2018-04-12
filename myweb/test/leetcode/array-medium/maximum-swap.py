#coding:utf8


class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = list(str(num))
        check = {}
        for index,i in enumerate(num):
            check[i]=index
        num_sort = sorted(num,reverse=True)
        for i in range(len(num)):
            m = num_sort[i]
            if m>num[i]:
                num[check[m]]=num[i]
                num[i]=m
                break
        return int(''.join(num))

s = Solution()
print s.maximumSwap(1273)