#coding:utf8
import datetime
from oslo_utils import timeutils

def martul(pic='#', num=20):
    try:
        print pic * num
    except:
        print '#'*20
    return

#UTC时间
utc_time = timeutils.utcnow()
print 'type:',type(utc_time)
print utc_time
print str(utc_time).split()

martul()
utc_time_t = timeutils.utcnow(True)
print 'type:',type(utc_time_t)
print utc_time_t

martul()
utc_time_2 = datetime.datetime.utcnow()
print utc_time_2
print utc_time_2 == utc_time

#当前时间
martul()
now_time = datetime.datetime.now()
print now_time

#时间差
martul()
print timeutils.delta_seconds(utc_time, now_time),'seconds'

martul()
print timeutils.is_newer_than(now_time, 22)
print now_time - utc_time
print datetime.timedelta(seconds=3)

martul()
print timeutils.isotime(now_time, True)

import uuid
from oslo_utils import uuidutils


martul()
uuid_new = uuidutils.generate_uuid()
uuid_dash = uuidutils.generate_uuid(False)
print 'uuid:',uuid_new,'length:',len(uuid_new)
print 'uuid dashed=False:',uuid_dash,'length:',len(uuid_dash)

martul()
print 'is uuid like:',uuidutils.is_uuid_like('11111111111111111111111111dddddd')
print 'is uuid like:',uuidutils.is_uuid_like('u9118604-7651-4fa8-9f65-c51cf91b4984')

def _format_uuid_string(string):
    return (string.replace('urn:', '')
                  .replace('uuid:', '')
                  .strip('{}')
                  .replace('-', '')
                  .lower())
#去掉'-'
print _format_uuid_string('u9118604-7651-4fa8-9f65-c51cf91b4984')
#返回带'-' 的
print uuid.UUID('19f3e3bb-8258-4b7e9-c3a-7765c6a7e694')

from oslo_utils import versionutils

martul()
print versionutils.convert_version_to_int('12.2')
print versionutils.convert_version_to_int(3)
print versionutils.convert_version_to_str(12.2)

from oslo_utils import strutils

martul()
TRUE_STRINGS = ('1', 't', 'true', 'on', 'y', 'yes')
print TRUE_STRINGS
print strutils.bool_from_string(1)
print strutils.bool_from_string('g')

martul()
print strutils.check_string_length('f',max_length=1)#???????

martul()
print strutils.int_from_bool_as_string('p')
print int(True)

martul()
print strutils.is_int_like(1)

martul()
#!!!!!!!!!!!!!!!!!!!
print strutils.mask_dict_password({'password':'sdfs','sdf':{'password':'fds','gg':{'password':'sdf'}}})
print strutils.mask_password('"password":"1213"')
#print strutils.string_to_bytes('ff')

from oslo_context import context

context.RequestContext()
