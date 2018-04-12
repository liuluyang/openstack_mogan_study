#coding:utf8


class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        #print nums
        count = 0
        i,j=0,1
        length = len(nums)-1
        temp = {}
        while j<length:
            m = nums[i]+nums[j]
            sub_count = 0
            if m not in temp:
                for num in nums[j+1:]:
                    if m>num:
                        sub_count+=1
                    else:
                        break
                if sub_count>0:
                    temp[m]=[sub_count,j]
                    count+=sub_count
            else:
                t = temp[m][-1]
                if t!=j:
                    temp[m][0]-=j-t
                    temp[m][-1]=j
                if temp[m][0] > 0:
                    count+=temp[m][0]
            #print nums[j],temp
            if i+1==j:
                i=0
                j+=1
            else:
                i+=1

        return count


s = Solution()
print s.triangleNumber([2,2,3,4])
print s.triangleNumber([1,2,3,4,5,6])

print s.triangleNumber([70,36,24,41,80,84,7,65])