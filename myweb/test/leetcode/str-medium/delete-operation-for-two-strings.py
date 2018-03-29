#coding:utf8


class Solution(object):
    def minDistance(self, w1, w2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        eat sea
        """
        # def t(X,Y,i,j,temp):
        #     if (i,j) in temp:
        #         return temp[(i,j)]
        #     if i<0 or j<0:
        #         ret = 0
        #     elif X[i]!=Y[j]:
        #         ret = max(t(X,Y,i-1,j,temp),t(X,Y,i,j-1,temp))
        #     else:
        #         ret = t(X,Y,i-1,j-1,temp)+1
        #     temp[(i,j)]=ret
        #     return ret
        #
        # l1 = len(w1)
        # l2 = len(w2)
        # #print l1+l2
        # return l1+l2-t(w1, w2, l1 - 1, l2 - 1, {}) * 2

        w1_len = len(w1)
        a = [0]*(w1_len+1)
        for s in w2:
            b = [0]*(w1_len+1)
            for i in range(w1_len):
                if s==w1[i]:
                    b[i+1]=a[i]+1
                else:
                    b[i+1]=max(b[i],a[i+1])
            a = b
        return w1_len+len(w2)-a[-1]*2


s= Solution()
print s.minDistance('abce','be')

print s.minDistance("pvhvykrvntdywrhylaprgqmbzqitrhdmxboyw","oelftlrthdmlwznwuritwrvdciho")
