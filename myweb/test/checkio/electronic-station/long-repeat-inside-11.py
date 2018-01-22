#coding:utf8
import re

def checkio(text):

    sub_str = []
    for num in range(len(text)//2):
        for i in range(len(text)):
            s = text[i:i+num+1]
            if len(s)==num+1:
                sub_str.append(s)
            else:
                break
    print sub_str
    for i in set(sub_str):
        s = re.findall(r'(('+i+'){2,})',text)
        if s:
            print i,s

print checkio('aabcabcaaa')