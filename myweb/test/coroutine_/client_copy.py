# -*- coding:utf-8 -*-

import time
from socket import *

ADDR, PORT = 'localhost', 8001

def main():
    while 1:
        client = socket(AF_INET,SOCK_STREAM)
        try:
            client.connect((ADDR, PORT))
            cmd = raw_input('>>:').strip()
            if len(cmd) == 0: continue
            for i in range(10):
                time.sleep(1)
                client.send(cmd)
                data = client.recv(1024)
                print data
            #print('Received', repr(data))
        except:
            print 'connection is done\ntrying connect...\nsuccess'
            continue

#client.close()
if __name__ == '__main__':
    main()