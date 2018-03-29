#coding:utf8


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        1.1.2
        1.1.0
        """
        v1 = version1.split('.')
        v2 = version2.split('.')
        max_length = max(len(v1),len(v2))
        v1.extend(['0']*(max_length-len(v1)))
        v2.extend(['0'] * (max_length - len(v2)))
        for i in range(max_length):
            a = int(v1[i])
            b = int(v2[i])
            if a!=b:
                if a>b:
                    return 1
                if a<b:
                    return -1
        return 0
