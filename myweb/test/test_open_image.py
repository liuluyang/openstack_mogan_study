#coding:utf8

import base64
open_icon = open("timg.png","rb")
print open_icon
b64str = base64.b64encode(open_icon.read())
print b64str