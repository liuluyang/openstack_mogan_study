#coding:utf8


class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        def make_num(num):
            return (num+1)*num/2
        all_count = 0
        not_need = 0

        temp1=0
        temp2=0
        for num in A:
            if num<L:
                temp2+=1
            else:
                not_need+=make_num(temp2)
                temp2=0
            if num<=R:
                temp1+=1
            else:
                all_count+=make_num(temp1)
                temp1=0
        print all_count
        return all_count+make_num(temp1)-not_need-make_num(temp2)

s = Solution()
print s.numSubarrayBoundedMax([1,2,4,2],2,3)