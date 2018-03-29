#coding:utf8


import random
# class Solution(object):
#     def maxsum(self,nums):
#         def t(nums,n,i,j):
#             if i==n:
#                 return nums[i][j]
#             return nums[i][j]+max(t(nums,n,i+1,j),t(nums,n,i+1,j+1))
#         n = len(nums)-1
#         return t(nums,n,0,0)
#         pass

# class Solution(object):
#     def maxsum(self,nums):
#         def t(nums,n,i,j,temp):
#             if i==n:
#                 return nums[i][j]
#             if str(i)+str(j) in temp:
#                 return temp[str(i)+str(j)]
#             v = nums[i][j]+max(t(nums,n,i+1,j,temp),t(nums,n,i+1,j+1,temp))
#             temp[str(i)+str(j)]=v
#             return v
#         n = len(nums)-1
#         temp = {}
#         return t(nums,n,0,0,temp)
#         pass


class Solution(object):
    def maxsum(self,nums):
        last = nums.pop()
        while nums:
            check = nums.pop()
            for i in range(len(check)):
                last[i]=max(last[i],last[i+1])+check[i]
            last.pop()
        return last[0]
        pass

nums = [[random.randint(0,9) for j in range(i)] for i in range(1,50)]
print nums
s = Solution()
print s.maxsum(nums)
