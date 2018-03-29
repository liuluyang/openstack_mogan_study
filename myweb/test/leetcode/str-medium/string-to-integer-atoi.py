#coding:utf8

import re
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if not str:
            return 0
        num = ''
        # ind = 0
        # for index, i in enumerate(str):
        #     if i.isdigit() or i in '+-':
        #         ind = index
        #     else:
        #         #ind = index
        #         break
        # num = str[0:ind+1]
        m = re.search(r'^[-+]*\d*', str)
        num = m.group()
        print num
        try:
            num = int(num)
            if num > 2147483647:
                return 2147483647
            if num < -2147483648:
                return -2147483648
            return num
        except:
            return 0

s = Solution()
print s.myAtoi("  010")