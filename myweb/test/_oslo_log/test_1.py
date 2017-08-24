#coding:utf8
from oslo_config import cfg

CONF = cfg.CONF

service_opts = [
    cfg.StrOpt('name',
               default='wechat',
               help='this is service name'
               ),
    cfg.StrOpt('style',
               default='app',
               help='this is style'
    )
]

group_opt = cfg.OptGroup(
            name='server',
            title='this is group name'
)

app_opts = [
    cfg.StrOpt(
        'host',
        default='0.0.0.0',
        help='this is server host'
    ),
    cfg.IntOpt(
        'port',
        default='9001',
        help='this is port'
    ),
    cfg.IntOpt(
        'workers',
        default='101',
        help='this is workers'
    )
]

def register_opts(conf):
    conf.register_opts(service_opts)
    conf.register_group(group_opt) #注册选项组
    conf.register_opts(app_opts, group_opt) #选项列表与选项组关联
    conf.register_opts(app_opts, group='server')
    conf.register_opts(app_opts, group='serveru')
register_opts(CONF)

#加载配置文件来覆盖默认配置选项
#如果被覆盖的默认选项不存在会报错
CONF(default_config_files=['app.conf'])

print CONF.name
print 'server host:',CONF.server.host
print 'serveru host:',CONF.serveru.host
print 'server group:',CONF.server