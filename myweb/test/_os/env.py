import os

env = os.environ
print env

for x,y in env.items():
    print (x.lower(),y)

s = ' d'
print s
s = s.strip()
print s

import oslo_utils.timeutils as timeutils
import six
def _time(timestamp=None):
    if not timestamp:
            timestamp = timeutils.utcnow()
            print timestamp
    if isinstance(timestamp, six.string_types):
        timestamp = timeutils.parse_strtime(timestamp)
        return timestamp

print _time()

import datetime
print datetime.datetime(1,1,1)