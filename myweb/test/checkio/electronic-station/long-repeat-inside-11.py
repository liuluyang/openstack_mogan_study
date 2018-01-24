# coding:utf8
import re


def checkio(text):
    sub_str = []
    for num in range(len(text) // 2):
        for i in range(len(text)):
            s = text[i:i + num + 1]
            if len(s) == num + 1:
                sub_str.append(s)
            else:
                break
    print sub_str
    result = ''
    for i in set(sub_str):
        s = re.findall(r'((' + i + '){2,})', text)
        if s:
            # print i,s
            for t in s:
                if len(t[0]) > len(result) or len(t[0]) == len(
                        result) and text.index(t[0]) < text.index(result):
                    result = t[0]
    return result


print checkio('aabcabcaaaaaa')
print checkio('qbc')


print checkio('aaaaa') == 'aaaaa'
print checkio('aabbff') == 'aa'
print checkio('aababcc') == 'abab'
print checkio('abc') == ''
print checkio('abcabcabab') == 'abcabc'