#coding:utf8
'''
问题：
从指定列表中找出两个数 两数之和等于给出的指定的某一整数
返回两数在列表中的索引值

len(nums)>=2

'''


from itertools import permutations,combinations
from copy import deepcopy
#注：同一个数不能用两次

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        '''
        nums_use = [num for num in nums if num<=target-sorted(nums)[0]]
        nums_per = combinations(nums_use, 2) #该结果只能用一次
        #print list(nums_per)
        for num in nums_per:
            #print sum(num)
            if sum(num)==target:
                if num[0]!=num[1]:
                    return [nums.index(num[0]),nums.index(num[1])]
                else:
                    return [nums.index(num[0]),nums.index(num[1],nums.index(num[0])+1)]
        '''
        nums_copy = deepcopy(nums)
        for n in sorted(nums_copy):
            second = target-n
            one_index = nums.index(n)
            if n!=second:
                try:
                    return [one_index,nums.index(second)]
                except:
                    continue
            else:
                try:
                    return [one_index,nums.index(second,one_index+1)]
                except:
                    pass


s = Solution()
print s.twoSum([1,2,3,4,5],5)
print s.twoSum([0,0],0)
print s.twoSum(range(0,30000,2),12822)