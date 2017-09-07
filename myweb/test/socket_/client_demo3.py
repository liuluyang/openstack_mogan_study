# -*- coding:utf-8 -*-

import time
from socket import *

ADDR, PORT = 'localhost', 9001


def connect_func():
    try:
        client = socket(AF_INET, SOCK_STREAM)
        client.connect((ADDR, PORT))
        return client
    except:
        print 'can not connect to server!'
        return


def main():
    client = connect_func()
    while 1:
        try:
            if client:
                cmd = raw_input('>>:').strip()
                if len(cmd) == 0: continue
                if cmd == 'exit': break
                client.send(cmd)
                data = client.recv(1024)
                print data
        except:
            client = connect_func()
            client.send(cmd)
            data = client.recv(1024)
            print data
    client.close()


if __name__ == '__main__':
    main()
