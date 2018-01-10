#coding:utf8
from itertools import groupby

'''
这个任务是这个系列中的第一个。在这里你应该找到字符串中最长的相同字符重复出现的次数，
并返回它的重复次数。例如：字符串“aaabbcaaaa”包含具有相同字母“aaa”，
“bb”，“c”和“aaaa”的四个子字符串。 最后一个子字符串是最长的一个字符串，你应该返回 4
'''

def checkio(line):
    now_s = None
    now_num = 0
    num_list = [0]
    for i in range(len(line)):
        if line[i] != now_s:
            now_num = 0
            now_s = line[i]
        now_num +=1
        num_list.append(now_num)
    num_list.sort()
    return num_list[-1]

print checkio('aa')

def long_repeat(line):
    return max((sum(1 for _ in g) for k, g in groupby(line)))
    #python3 max()增加了default参数

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    print('"Run" is good. How is "Check"?')