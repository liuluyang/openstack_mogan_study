from routes import Mapper

map = Mapper()
print map
print type(map)

#4.conditions  conditions=dict(method=['GET', 'HEAD'])
map.connect('/user/list', controller = 'user', action = 'list', conditions={'method' : ['GET', 'HEAD']})
result = map.match('/user/list')

#
map.connect(r'/blog/{id:\d+}')
map.connect(r'/download/{platform:windows|linux/{filename}')
map.connect(r'/blog/{id}', requirements={'id':r'\d+'})
map.connect(r'/blog/{platfrom}/{filename}', requirements={'platform':r'windows|linux'})

print result


#5. {.format}
map.connect('/entries/{id}{.format}', controller = 'main', action = 'index')

map.connect('/entries/{id}{.format:mp8}', controller = 'main', action = 'index')
result = map.match('/entries/50.mp3')