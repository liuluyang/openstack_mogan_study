
import re

ip = '10.218.132.7'

ip = ip.replace('.', '\.')
print ip
ip_obj = re.compile(ip)

print ip_obj

print ip_obj.match('10.218.132.7')