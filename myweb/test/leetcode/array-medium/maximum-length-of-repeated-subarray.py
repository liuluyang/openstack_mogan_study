#coding:utf8


class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        # max_len = 0
        # length =len(B)
        # index = 0
        # while length-index>max_len:
        #     old_num = B[index]
        #     new_index = index
        #     num = B[new_index]
        #     sub_len = 0
        #     for i in A:
        #
        #         if i==num:
        #             sub_len+=1
        #             max_len = max(sub_len,max_len)
        #             #print 'max',max_len
        #             new_index+=1
        #             try:
        #                 num = B[new_index]
        #             except:
        #                 break
        #
        #         else:
        #             sub_len = 0
        #             new_index = index
        #             num = old_num
        #     index +=max_len
        # return max_len

        lengthA = len(A)
        result = 0
        temp = [0]*(lengthA+1)
        for b in B:
            temp2 = [0]
            for index in range(lengthA):
                if b==A[index]:
                    temp2.append(temp[index]+1)
                else:
                    temp2.append(0)
            print temp2
            result = max(result,max(temp2))
            temp = temp2
        return result


s = Solution()
print s.findLength([1,2,3,2,1],[3,2,1,4,7])
print s.findLength([0,0,0,0,1],[1,0,0,0,0])