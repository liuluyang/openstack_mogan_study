#coding:utf8

import socket
import eventlet
from eventlet import greenthread
from multiprocessing import Pool, Process
import gevent
from gevent import monkey;monkey.patch_all()

host = '127.0.0.1'
port = 9001

def t(conn):
        while True:
            data = conn.recv(1024)
            if not data:
                continue
            print 'revice :',data
            conn.sendall('success')

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    conn, addr = s.accept()
    print conn,addr
    conn_2, addr_2 = s.accept()
    print conn_2,addr_2

    while True:
            data = conn.recv(1024)
            if not data:
                conn.sendall('again_conn')
            conn.sendall(data)
            d = conn_2.recv(1024)
            if not d:
                conn.sendall('again_conn_2')
            conn_2.send(d)

    #p = Process(target=t, args=(conn,))
    #p = Process(target=t, args=(conn,))
    #conn.close()
    #gevent.spawn(t, conn)

if __name__ == '__main__':
    main()
