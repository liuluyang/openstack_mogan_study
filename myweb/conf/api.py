#coding:utf8

import sys
from oslo_config  import cfg

opts = [
    cfg.HostAddressOpt('host_ip',
                       default='0.0.0.0',
                       help='the ip address on which mogan-api listens'
                       ),
    cfg.PortOpt('port',
                default='6688',
                help='the tcp port on which mogan-api listens'
                )
]

opt_group = cfg.OptGroup(name='api',
                         title='options for the mogan-api service'
                         )

def register_opts(conf):
    conf.register_group(opt_group)
    conf.register_opts(opts, group=opt_group)