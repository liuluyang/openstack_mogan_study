from oslo_log import log as logging
from oslo_config import cfg
from oslo_utils import netutils

LOG = logging.getLogger(__name__)
#CONF = cfg.CONF
#DOMAIN = "demo"

#logging.register_options(CONF)
#logging.setup(CONF, DOMAIN)

class Hydrant(object):
    def __init__(self, in_arg):
        self.in_arg = in_arg

    def __call__(self, environ, start_response):
        print 'Hydrant'
        start_response('200 ok', [('Content Type', 'text/plain')])
        LOG.debug('this is hydrant')
        print netutils.get_my_ipv4()
        return ['%s, %s!\n' % (self.in_arg, 'Hydrant')]

def app_factory(global_config, in_arg):
    print 'hydrant',global_config
    return Hydrant(in_arg)