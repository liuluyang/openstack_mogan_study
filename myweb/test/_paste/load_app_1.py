from paste import httpserver
from paste.deploy import loadapp

if __name__ == '__main__':
    httpserver.serve(loadapp('config:api_conf.ini', relative_to = '.'), host = '127.0.0.1', port=8001)