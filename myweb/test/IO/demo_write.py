#coding:utf8


def write(name):
    with open(name, 'a+') as f:
        f.write('\nhello world!\nwelcome\n你好')


write('w.txt')