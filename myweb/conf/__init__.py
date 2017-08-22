#coding:utf8

from oslo_config import cfg

from myweb.conf import api

CONF = cfg.CONF  # => ConfigOpts()

api.register_opts(CONF)

print CONF.api.host_ip