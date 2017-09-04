#coding:utf8


def write(name):
    with open(name, 'a+') as f:
        f.write('\nhello world!\nwelcome')


write('w.txt')