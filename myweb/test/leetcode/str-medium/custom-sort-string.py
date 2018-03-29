#coding:utf8

from collections import OrderedDict
class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        # result = ''
        # t = list(T)
        # for s in S:
        #     while True:
        #         try:
        #             t.remove(s)
        #         except:
        #             break
        #         result+=s
        # return result+''.join(t)
        last = ''
        order = OrderedDict(zip(S,[0]*len(S)))
        print order
        for s in T:
            if s in order:
                order[s]+=1
            else:
                last+=s
        start = ''
        for s,num in order.items():
            start+=s*num
        return start+last


s = Solution()
print s.customSortString('abc','cadb')