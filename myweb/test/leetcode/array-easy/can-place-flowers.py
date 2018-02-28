#coding:utf8


class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flowerbed.insert(0,0)
        flowerbed.insert(0,1)
        flowerbed.append(0)
        flowerbed.append(1)
        result = 0
        num = 0
        for i in flowerbed:
            if i==1 and num>0:
                result+=(num-1)/2
                num = 0
            if i==0:
                num+=1
        return result>=n

s = Solution()
print s.canPlaceFlowers([1,0,0,0,1],1)
print s.canPlaceFlowers([0,0,1,0,1,0,0,0,],1)

