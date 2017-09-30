#coding:utf8

import socket

host = '127.0.0.1'
port = 8080
s = socket.socket()
s.connect((host, port))
def main():
    while True:
        try:
            #content = raw_input('>>>')
            #s.send(content)
            d = s.recv(1024)
            if d:
                print '>>',d
            continue
        except:
            break


main()