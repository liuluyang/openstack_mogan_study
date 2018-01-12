#coding:utf8

import re

#I thought this is the best solutions
#思路：
#1.先找出可能需要修改的字符串
#2.在正确的金额中小数点‘.’最多只会有一个
#3.所以把含有分隔符的金额先全部换成‘,’再进行判断做进一步修改
def checkio(text):
    numbers =  re.findall('(?<=\$)[^ ]*\d', text)
    #print numbers
    for old in numbers:
        new = old.replace('.', ',')
        if ',' in new and len(new.split(',')[-1]) == 2:
            print new
            print new.rsplit(',', 1)
            new = '.'.join(new.rsplit(',', 1))
        # if old==new:
        #     print True
        # else:
        #     print False
        text = text.replace(old, new)
        #print text
    return text

# print checkio('Clayton Kershaw $31.000.000\nZack Greinke   $27.000.000\nAdrian Gonzalez $21.857.143\n')
# print checkio("Lot 192.001 costs $1.000,94.")
# print checkio('$12.123')
print checkio('$12.212,13  $12.212,13')
#扩展判断金额格式对不对