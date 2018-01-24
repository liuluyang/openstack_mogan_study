#coding:utf8

import urllib2

url = 'https://www.baidu.com'
r = urllib2.urlopen(url, timeout=5)
print r.read()