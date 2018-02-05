#coding:utf8

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #return [n for i,n in enumerate(nums) if i>=1 and n!=nums[i-1] or i==0]
        # if not A:
        #     return 0
        #
        # newTail = 0
        #
        # for i in range(1, len(A)):
        #     if A[i] != A[newTail]:
        #         newTail += 1
        #         A[newTail] = A[i]
        # print A
        #
        # return newTail + 1
        nums[0:len(set(nums))] = list(set(nums))
        print nums
        return len(set(nums))


s = Solution()
print s.removeDuplicates([1,1,2,2,2,4])