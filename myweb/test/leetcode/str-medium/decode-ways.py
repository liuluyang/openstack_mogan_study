#coding:utf8

import re
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        1-26
        1-9
        10 20
        '147148142'
        0 3 4
        '123'->1 23, 12 3 ,1 2 3
        '1037'-> 10 3 7,
        '12'->1 2, 12
        '2345'->2 3 4 5, 23 4 5,
        '11023'-> 1 10 2 3, 1 10 23
        '101011'-> 10 10 1 1, 10 10 11
        10 10 1 1
        123 ->1 2 3
        12 3
        1 23
        1281-> 1 2 8 1
        12 8 1
        1223-> 1 2 2 3
        12 2 3
        12 23
        1 22 3
        1 2 23
        index:0 1 2
        1: 3
        2: 0 1, 1 2, 0 2,
        3:0 1 2
        12201023
        1223211221
        0 1 2 4 5 6 7 8
        """
        def test(s):
            length = len(s)
            count = 0
            check = [0]
            while check:
                index = check.pop(0)

                for i in range(1):
                    if index+1==length:
                        count+=1
                        break
                    else:
                        check.append(index+1)
                    next_num = int(s[index:index+2])
                    if next_num<=26 and index+2==length:
                        count+=1
                        break
                    elif next_num<=26:
                        check.append(index+2)
            return count

        if s[-1]!='0':
            s+=s[-1]+'0'
        result = 1
        s = s.split('0')
        print s
        for sub in s:
            if sub[0:-1]:
                result*=test(sub[0:-1])

        return result




s = Solution()
print s.numDecodings('121212')

