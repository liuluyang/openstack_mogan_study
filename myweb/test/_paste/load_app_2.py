from wsgiref.simple_server import make_server
from wsgiref.simple_server import make_server
from wsgiref.simple_server import make_server
from paste import httpserver
from paste.deploy import loadapp
from paste.deploy import loadapp
from paste.deploy import loadapp
import os
import paste.urlmap

if __name__ == '__main__':
    configfile = 'api_conf.ini'
    #appname = 'main'

    appname = 'metadata'
    print os.path.abspath(configfile)
    wsgi_app = loadapp('config:%s' % os.path.abspath(configfile), appname)

    #httpserver.serve(loadapp('config:configure.ini', relative_to = '.'), host = '127.0.0.1', port=8000)

    server = make_server('localhost', 8000, wsgi_app)
    print 'service is running ....'
    server.serve_forever()

import paste.urlmap
