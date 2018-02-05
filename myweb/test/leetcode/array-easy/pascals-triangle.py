#coding:utf8


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==1:
            return [[1]]
        if numRows==2:
            return [[1],[1,1]]

        result = [[1],[1,1]]
        while numRows-2>0:
            numRows -= 1
            sub_row = []
            for i,n in enumerate(result[-1]):
                try:
                    sub_row.append(n+result[-1][i+1])
                except:
                    pass
            sub_row.insert(0,1)
            sub_row.append(1)
            result.append(sub_row)
        return result

s = Solution()
print s.generate(5)


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1]
        for i in range(0, rowIndex):
            res = map(lambda x, y: x+y, res + [0], [0] + res)
        return res


s = Solution()
print s.getRow(5)