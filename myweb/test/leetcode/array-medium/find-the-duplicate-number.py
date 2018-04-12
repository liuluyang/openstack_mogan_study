#coding:utf8



class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # temp = set([])
        # result = set([])
        # for i in nums:
        #     if i in temp:
        #         result.add(i)
        #     else:
        #         temp.add(i)
        #
        # if len(result)==1:
        #     return result.pop()
        # else:
        #     return None

        temp = set([])
        result = None
        for i in nums:
            if i not in temp:
                temp.add(i)
            else:
                if result==None:
                    result = i
                elif result!=None and result!=i:
                    return None
                else:
                    pass
        return result

s = Solution()
print s.findDuplicate([1,1])
