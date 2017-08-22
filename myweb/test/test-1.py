#coding:utf8
from oslo_config import cfg
from oslo_config import types

PortType = types.Integer(1, 65535)
# 定义一组选项
common_opts = [
    cfg.StrOpt('bind_host',
               default='0.0.0.0',
               help='IP address to listen on.'),
    cfg.Opt('bind_port',
            type=PortType,
            default=9292,
            help='Port number to listen on.')
]


import logging

def add_common_opts(conf):   # 注册选项
        conf.register_opts(common_opts)


def get_bind_host(conf):   # 使用选项
        return conf.bind_host


def get_bind_port(conf):
        return conf.bind_port

# 创建配置类
cf = cfg.CONF
print cf
# 开始注册
add_common_opts(cf)
print cf.bind_host
print(get_bind_host(cf))