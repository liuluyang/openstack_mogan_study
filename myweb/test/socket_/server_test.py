# coding:utf8

import socket
import gevent
from gevent import monkey

monkey.patch_all()


def socket_obj():
    host_port = ('127.0.0.1', 9001)
    sock = socket.socket()
    sock.bind(host_port)
    sock.listen(1)
    print 'listening on 127.0.0.1:9001...'
    while True:
        conn, addr = sock.accept()
        print conn
        gevent.spawn(conn_obj, conn)


def conn_obj(conn):
    try:
        while True:
            revice_data = conn.recv(1024)
            conn.send(revice_data)
    except Exception as e:
        print e


if __name__ == '__main__':
    socket_obj()
