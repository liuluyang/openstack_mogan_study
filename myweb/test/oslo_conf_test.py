from oslo_config import cfg

CONF = cfg.CONF

test_opt = [
    cfg.StrOpt(
        'name',
        default='myweb',
        help=('this is help for name')
    ),
    cfg.IntOpt(
        'worker',
        default=5,
        help=('this is num of workers')
    )

]

test_group = cfg.OptGroup('project', title='this is project')

def register_opt(conf):
    conf.register_group(test_group)
    conf.register_opts(test_opt, group=test_group)

register_opt(CONF)

print CONF.project.name
print CONF.project.worker

c = cfg.CONF
print c.project.name

dest = cfg.StrOpt(
        'name',
        default='myweb',
        help=('this is help for name')
    )

print dest.name
print dest.dest

