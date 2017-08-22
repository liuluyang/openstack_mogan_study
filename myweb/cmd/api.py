from wsgiref import simple_server

from myweb.api import app


def main():
    host = '0.0.0.0'
    port = 9001
    application = app.setup_app()
    srv = simple_server.make_server(host, port, application)
    print 'mytest runing on 9001 ....'
    srv.serve_forever()


if __name__ == '__main__':
    main()