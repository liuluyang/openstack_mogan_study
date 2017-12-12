from wsgiref import simple_server

from myweb.api import app


def main():
    host = '0.0.0.0'
    port = 9001
    application = app.setup_app()
    srv = simple_server.make_server(host, port, application)
    print 'mytest running on 9001 ....'
    register_conf()
    srv.serve_forever()


def register_conf():
    from oslo_config import cfg
    from myweb.conf.api import register_opts
    conf = cfg.CONF
    register_opts(conf)

def  main_2():
    host = '0.0.0.0'
    port = 9002
    application = app.set_app()
    server = simple_server.make_server(host, port, application)
    print 'runnnig in 9002'
    register_conf()
    server.serve_forever()


if __name__ == '__main__':
    main()
    #main_2()
    # from multiprocessing import Pool
    # l = [main, main_2]
    # p = Pool()
    # for i in l:
    #     p.apply_async(i)
    # p.close()
    # p.join()


