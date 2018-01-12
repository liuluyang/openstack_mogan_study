#coding:utf8

'''
您需要找到所有唯一字母的第一个最长的子字符串
abcdag
'''

def checkio(text):
    text_list = []
    for i in range(len(text)):
        num = 0
        long_str = ''
        for s in text[i:]:
            if s not in long_str:
                num+=1
                long_str+=s
                if len(long_str)==len(text[i:]):
                    text_list.append((num, long_str))
            else:
                text_list.append((num, long_str))
                break
    print text_list
    max_str = max([i[0] for i in text_list])
    long_non_repeat = ''
    for num, text in text_list:
        if num==max_str:
            long_non_repeat =text
            break
    return long_non_repeat

print checkio('abdjwawk')
print checkio('ws')

#the best solution
def non_repeat(line):
    result = ''
    for i in range(len(line)):
        s = ''
        for c in line[i:]:
            if c in s:
                break
            s += c
        if len(s) > len(result):
            result = s
    return result

print non_repeat('abdjwawk')
print non_repeat('ws')