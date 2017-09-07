# -*- coding:utf-8 -*-


import sys
import socket
import gevent
from gevent import monkey
monkey.patch_all()

def server(port):
    sock = socket.socket()
    sock.bind(('127.0.0.1', port))
    sock.listen(500)
    while 1:
        conn, addr = sock.accept()
        #handle_request(conn)
        gevent.spawn(handle_request, conn)


def handle_request(conn):
    try:
        while 1:
            data = conn.recv(1024)
            if not data:
                break
            print("recv:",data)
            conn.send(data)

    except Exception as ex:
        print(ex)
    finally:
        conn.close()

if __name__ == '__main__':
    server(8001)