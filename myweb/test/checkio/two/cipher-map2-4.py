#coding:utf8

import numpy as np

n = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
])

v = np.rot90(n, 4)

print n

print v

for n,i in enumerate(v):
    for m,y in enumerate(i):
        if y==6:
            print (n,m)

def recall_password(posti,mod):
    posti_array = [list(i) for i in posti]
    mod_array = [list(i) for i in mod]
    posti_list = []
    password = ''
    print posti_array
    print mod_array
    p = np.array(posti_array)
    for i in range(4):
        v = np.rot90(p,4-i)
        for n,i in enumerate(v):
            for m,y in enumerate(i):
                if y=='X':
                    posti_list.append((n,m))
    print posti_list
    for i,y in posti_list:
        password +=mod_array[i][y]
    print password


recall_password(
    ('X...',
     '..X.',
     'X..X',
     '....'),
    ('itdf',
     'gdce',
     'aton',
     'qrdi')) #== 'icantforgetiddqd'
