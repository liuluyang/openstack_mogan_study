#coding:utf8


class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        727475 2796
                2976
               2967
        727475 6279

        7274752649
        7274752694

        2976
        9267#error
        6279

        """
        # change_num = None
        # nums = str(n)
        # for index in xrange(1,len(nums)):
        #     if int(nums[-index])>int(nums[-index-1]):
        #         change_num = int(nums[-index-1])
        #         start = nums[:-index-1]
        #         last = sorted(nums[-index-1:])
        #         for num in last:
        #             if int(num)>change_num:
        #                 last.remove(num)
        #                 start+=num+''.join(last)
        #                 result = int(start)
        #                 if result>2**31-1:
        #                     return -1
        #                 else:
        #                     return result
        # return -1
        change_num = None
        nums = map(int,str(n))
        for index in xrange(1, len(nums)):
            change_index = -index-1
            if nums[-index] > nums[change_index]:
                change_num = nums[change_index]
                start = nums[:change_index]
                last = sorted(nums[change_index:])
                for num in last:
                    if num > change_num:
                        last.remove(num)
                        start.append(num)
                        start.extend(last)
                        result = 0
                        for i in start:
                            result = result*10+i
                        if result > 2 ** 31 - 1:
                            return -1
                        else:
                            return result
        return -1

s = Solution()
print s.nextGreaterElement(12443322)
