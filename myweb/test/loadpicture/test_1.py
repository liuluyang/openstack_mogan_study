#coding:utf8

import urllib2

url = 'https://www.baidu.com'
u = 'http://51.alook.pw/media/photos/1394.jpg'
r = urllib2.urlopen(u, timeout=5)
print r.read()