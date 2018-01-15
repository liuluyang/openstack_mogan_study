#coding:utf8

'''
该功能应识别主题行是否有压力。紧张的主题行意味着所有的字母都是大写的，
并且/或者以至少3个惊叹号结尾，并且/或者包含以下“红”字“help”，“asap”，“urgent”中的至少一个。
任何这些“红色”单词都可以用不同的方式拼写 - “帮助”，“帮助”，“HeLp”，“H！E！L！P！”，“H-E-L-P”，
即使是非常懒惰的“HHHEEEEEEEEELLP”
'''
import re
def checkio(text):

    if text.isupper():
        return True
    if len(text)>=3 and text[-3:]=='!!!':
        return True
    s = text.lower()
    h = re.findall('h[h|\W]*e[e|\W]*l[l|\W]*p', s)
    a = re.findall('a[a|\W]*s[s|\W]*a[a|\W]*p', s)
    u = re.findall('u[u|\W]*r[r|\W]*g[g|\W]*e[e|\W]*n[n|\W]*t', s)
    if h or a or u:
        return True
    return False

print checkio('I neeed HELP')

import re

h = re.findall('h[h|!|\-]*e[e|!|\-]*l[l|!|\-]*p', 'hell h-!!e!!l!!pd')
a = re.findall('a[a|!|\-]*s[s|!|\-]*a[a|!|\-]*p','')
u = re.findall('u[u|!|\-]*r[r|!|\-]*g[g|!|\-]*e[e|!|\-]*n[n|!|\-]*t','')
print h