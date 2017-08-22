from routes import Mapper

map = Mapper()
print map

map.connect('name', '/blog/{id}', controller='main', action='index')
result= map.match('/blog/1')
print result