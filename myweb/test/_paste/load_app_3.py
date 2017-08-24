from wsgiref.simple_server import make_server
from paste.deploy import loadapp
import os
from oslo_log import log as logging
from oslo_config import cfg

LOG = logging.getLogger(__name__)
CONF = cfg.CONF
DOMAIN = "demo"



if __name__ == '__main__':
    logging.register_options(CONF)
    logging.setup(CONF, DOMAIN)

    config = 'api_conf.ini'
    name = 'main'
    app = loadapp('config:%s'%(os.path.abspath(config)), name)
    server = make_server('localhost', 8000, app)
    server.serve_forever()

