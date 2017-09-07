# -*- coding:utf-8 -*-


import sys
import socket
import gevent
from gevent import monkey
monkey.patch_all()

def socket_obj():
    sock = socket.socket()
    return sock

def server(port):
    sock = socket.socket()
    sock.bind(('127.0.0.1', port))
    sock.listen(1)
    while 1:
        conn, addr = sock.accept()
        #handle_request(conn)
        gevent.spawn(handle_request, conn)   #可以接收多个连接
        #handle_request(conn)     #只能接收一个连接


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
