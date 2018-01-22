#coding:utf8

import re
tt = "Tina is a good girl, she is cooool, clever, and so on..."
rr = re.compile(r'\w*oo\w*')
print(rr.findall(tt))   #查找所有包含'oo'的单词

r2 = re.compile(r'((oo)+)')
print r2.findall(tt)

r3 = re.compile(r'Tina[\w|\s|\W]*')
print r3.match(tt).group()

s='1113446777'
m = re.findall(r'[0-9]',s)
print m

m = re.search(r'1+',s)
print m.group()