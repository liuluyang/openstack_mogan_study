#coding:utf8

def read(name):
    with open(name, 'r') as f:
        #print f.read()
        lines = f.readlines()
        for i,y in enumerate(lines):
            print i,y

        print f.readline(11)
read('desc.txt')