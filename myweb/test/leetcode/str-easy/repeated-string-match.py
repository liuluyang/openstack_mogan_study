#coding:utf8


class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        abcdf  abc dfa cdfab cdfa
        fa 2
        fabcd <=
        fabcdf 2
        fabcdfa 3
        fabcdfabcdfa 4
        """
        if len(set(B))>len(set(A)):
            return -1

        a_length = len(A)
        b_length = len(B)
        for i in range(1,b_length/a_length+2+1):
            if B in A*i:
                return i
        return -1

