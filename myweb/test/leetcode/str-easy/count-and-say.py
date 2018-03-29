#coding:utf8

import re
def countAndSay(n):
    '''
    1
    11
    21
    1211
    111221
    312211
    :param n:
    :return:
    '''
    s = '1'
    for _ in range(n - 1):
        s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)
    return s

print countAndSay(6)

from itertools  import groupby
def test(n):
    result = '1'
    print list(groupby(result))
    for i in range(n-1):
        r = ''
        for num,n in groupby(result):
            r+=str(len(list(n)))
            r+=str(num)
        result = r
    return result


print test(6)