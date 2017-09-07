#coding:utf8

import socket

host = '127.0.0.1'
port = 9001

def main():

    while True:
        s = socket.socket()
        try:
            s.connect((host, port))
            content = raw_input('>>>')
            s.send(content)
            d = s.recv(1024)
            print 'result :',d
        except:
            print 'connect again'


main()