#coding:utf8

import socket

host = '127.0.0.1'
port = 9001

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(2)
    conn, addr = s.accept()
    print conn,addr
    while True:
        data = conn.recv(1024)
        if not data:
            continue
        print 'revice :',data
        conn.sendall('success')
    #conn.close()

main()
