# -*- coding: utf-8 -*-
import sys
from oslo_config import cfg
from oslo_log import log as logging
import service

CONF = cfg.CONF
LOG = logging.getLogger(__name__)

def default_action(env, method, path, query, body):
    LOG.info("demo action (method:%s, path:%s, query:%s, body:%s)"
        % (method, path, query, body))
    return ("200 OK", "default")

def test_action(env, method, path, query, body):
    LOG.info("test (method:%s, path:%s, query:%s, body:%s)"
        % (method, path, query, body))
    return ("200 OK", "test")

if __name__ == "__main__":
    CONF(sys.argv[1:])
    host = getattr(CONF, "host", "0.0.0.0")
    port = getattr(CONF, "port", "8001")
    services = service.MiniService(host, port)
    services.add_action("", default_action)
    services.add_action("test", test_action)
    print 'running 9002'
    services.start()