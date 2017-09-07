# -*- coding:utf-8 -*-


from socket import *

ADDR, PORT = 'localhost', 8001
client = socket(AF_INET,SOCK_STREAM)
client.connect((ADDR, PORT))

while 1:
    cmd = raw_input('>>:').strip()
    if len(cmd) == 0: continue
    client.send(cmd)
    data = client.recv(1024)
    print data
    #print('Received', repr(data))

#client.close()