
from myweb.test.inbuild.hashlib_ import passwd_md5

list_ = [
    {
        'path':'/etc/bin',
        'cont':'dafadasdsa'
    },
    {
        'path':'/etc/bin/txt',
        'cont':'dafadasdfresa'
    }
]

inject = []
for i in list_:
    inject.append((i['path'],i['cont']))

print inject

def make_(f):
    k,y = f
    return k,passwd_md5(y)

print [make_(f) for f in inject]