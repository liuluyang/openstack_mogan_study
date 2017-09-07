#coding:utf8

import socket

host = '127.0.0.1'
port = 9001

def main():
    s = socket.socket()
    s.connect((host, port))
    while True:
        content = raw_input('>>>')
        s.send(content)
        d = s.recv(1024)
        print 'result :',d
    #s.close()

main()