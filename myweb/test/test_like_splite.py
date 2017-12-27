#coding:utf8


#问题：'083e8e78a522'==>'08-3E-8E-78-A5-22'

s = '083e8e78a522'

new = '-'.join([s[i:2] for i in range(0,len(s),2)]).upper()

print  new