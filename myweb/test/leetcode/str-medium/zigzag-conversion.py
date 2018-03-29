#coding:utf8


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        0 q    4$$   6 k
        1 a   5 j  7 l
        2 d   6 h   8 m
        3 g   7 $$    9 e

        ww    oo
        qq jj  pp
        ee     ll

        kk ii
        pp  kk

        """

        check = []
        start = 0
        length = len(s)
        if length<=numRows or numRows==1:
            return s
        s = list(s)
        while True:
            a = []
            a = s[start:start+numRows]
            start = start+numRows
            if len(a)!=numRows:
                for i in range(numRows-len(a)):
                    a.append('#')
            check.append(a)
            if start>length:
                break

            b = ['#']
            b.extend(s[start:start+numRows-2])
            start = start+numRows-2
            if len(b)!=numRows:
                for i in range(numRows-len(b)):
                    b.append('#')
            check.append(b[::-1])
            if start>length:
                break
        print check
        result = ''
        for i in range(len(check[0])):
            for j in range(len(check)):
                if check[j][i]!='#':
                    result+=check[j][i]

        return result

s = Solution()
print s.convert('ABCDEFGHI',2)
'''
A   E   I
B D F H
C   G
'''
