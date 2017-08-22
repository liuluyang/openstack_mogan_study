#coding:utf8

import sys
reload(sys)
sys.setdefaultencoding('utf8')
import gettext

# 一些设置
gettext.install('messages','C:\Users\liuluyang\PycharmProjects\untitled\myweb\locale',unicode=False)
gettext.translation('messages','C:\Users\liuluyang\PycharmProjects\untitled\myweb\locale',languages=['zh_CN'])

#print _('hello world')