from routes import Mapper

map = Mapper()
print map
print type(map)

map.connect(None, '/error/{action}/{id}', controller='error')
result = map.match('/error/lixin/200')
print result

map.connect(None, '/error/{action:index|lixin}/{id:\d+}', controller='error')
result = map.match('/error/lixin/200')

print result