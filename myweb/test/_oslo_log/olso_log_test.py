#coding:utf8

from oslo_config import cfg
from oslo_log import log as logging

LOG = logging.getLogger(__name__)
CONF = cfg.CONF
DOMAIN = "demo"

logging.register_options(CONF)
logging.setup(CONF, DOMAIN)


def test():
    # Oslo Logging uses INFO as default
    LOG.info("Oslo Logging %s",111111)
    LOG.warning("Oslo Logging")
    LOG.error("Oslo Logging")

if __name__ == '__main__':
    test()
