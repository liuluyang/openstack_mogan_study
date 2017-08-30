
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

print passwd_md5('11')
print passwd_md5('11')
