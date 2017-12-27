#coding:utf8
import hashlib

_str = 'hello world'
_md5 = hashlib.md5()

_md5.update(_str)
_str_md5 = _md5.hexdigest()
print len(_str_md5),_str_md5

_str = '748274'
_md5 = hashlib.md5()

_md5.update(_str)
_str_md5 = _md5.hexdigest()
print len(_str_md5),_str_md5

import random
import json

#print '{:06}'.format(random.randint(0,999999))

#for i in range(1000000):
    #if '573453' == '{:06}'.format(random.randint(0,999999)):
        #print i


def passwd_md5(password):
    _md5 = hashlib.md5()
    _md5.update(password)
    _passwd_md5 = _md5.hexdigest()
    return _passwd_md5

print passwd_md5('方便。打个比方来说，所有的数据就好像许许多多的书本。如果这些书本是一本一本堆'
                 '起来的，就好像链表或者线性表一样，整个数据会显得非常的无序和凌乱，在你找到自己'
                 '需要的书之前，你要经历许多的查询过程；而如果你对所有的书本进行编号，并且'
                 '把这些书本按次序进行排列的话，那么如果你要寻找的书本编号是n，那么经过二分查找，你很快就会找'
                 '到自己需要的书本；但是如果你每一个种类的书本都不是很多，那么你就可以对这些书本进行归类，哪些'
                 '是文学类，哪些是艺术类，哪些是工科的，哪些是理科的，你只要对这些书本进行简单的归类'
                 '，那么寻找一本书也会变得非常简单，比如说如果你要找的书是计算机方面的书，那么你就会到工')
print passwd_md5('11')
