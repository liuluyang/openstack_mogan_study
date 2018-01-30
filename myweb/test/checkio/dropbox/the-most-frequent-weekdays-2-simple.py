#coding:utf8

'''

星期一 Mon Monday
星期二 Tue Tuesday
星期三 Wed Wednesday
星期四 Thu Thursday
星期五 Fri Friday
星期六 Sat Saturday
星期日 Sun Sunday
'''
weeks = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',
         'Sunday','Monday']

import datetime
print datetime.datetime.now().weekday()
start = datetime.datetime(2399,1,1)
print start.weekday()

def checkio(year):
    start = datetime.datetime(year,1,1).weekday()
    if year%400==0 and year%100==0 or year%100!=0 and year%4==0:
        result = weeks[start:start+366%7]
        return result if result!=['Sunday','Monday'] else ['Monday','Sunday']
    else:
        return weeks[start:start+365%7]
    pass


import calendar

def most_frequent_days(year):
    days = {calendar.weekday(year, 1, 1), calendar.weekday(year, 12, 31)}
    print days
    return [calendar.day_name[i] for i in sorted(days)]


print most_frequent_days(2018)

