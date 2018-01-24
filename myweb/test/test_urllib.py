#coding:utf8
import urllib2

def gethtml(url):

    data = urllib2.urlopen(url)
    h = data.read()
    print h

print gethtml('https://www.baidu.com/')
print gethtml('https://translate.google.cn')
