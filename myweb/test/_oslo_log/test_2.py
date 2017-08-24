#coding:utf8
from oslo_config import cfg
from oslo_config import types
from test_1 import CONF

PortType = types.Integer(1,65535)

common_opts = [
    cfg.StrOpt(
        'bind_host',
        default='0.0.0.0',
        help='ip address to listen on'
    ),
    cfg.Opt(
        'bind_port',
        type=PortType,
        default=9292,
        help='port number to listen on'
    )
]

server_name_opt = cfg.StrOpt(
    'server_name',
    default='qq',
    help='this is server name'
)

def register_opts(conf):
    conf.register_opts(common_opts)  #注册默认配置选项列表
    conf.register_opt(server_name_opt) #注册单个默认配置选项

cli_opts = [
    cfg.BoolOpt('verbose',
                short='v',
                default=False,
                help='Print more verbose output'),
    cfg.BoolOpt('debug',
                short='d',
                default=False,
                help='Print debugging output'),
]

def register_opts_cli(conf):
    #conf.register_opts(cli_opts) #
    conf.register_cli_opts(cli_opts) #通过命令行配置 window运行出错


register_opts(CONF)
#register_opts_cli(CONF)
print CONF.server_name, CONF.bind_port
