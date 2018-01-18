#coding:utf8

import re
import numpy as np

s = '2'
a = re.findall(r'['+s+']{4,}','fasd $12222,23.23, sa')
#print a


d = [
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]

def checkio(matrix):
    date_position = find_position(matrix)
    all_nums = [y for i in matrix for y in i]
    need_check_nums = [i for i in set(all_nums) if all_nums.count(i)>=4]
    for sub_data in date_position:
        for num in need_check_nums:
            print sub_data
            sub_data = [str(i) for i in sub_data]
            if re.findall(r'['+str(num)+']{4,}',''.join(list(sub_data))):
                return True

def find_position(data):
    n = np.array(data)
    v = np.rot90(n, 1)
    date_index = []
    date_nums = []
    width = len(data)
    for i in range(width-3):
        index_1 = []
        index_2 = []
        for x,y in enumerate(range(width)):
            if x+i<=width-1:
                index_1.append((x+i,y))
            if y+i<=width-1:
                index_2.append((x,y+i))
        date_index.append(index_1)
        date_index.append(index_2)
    # print date_index
    # print n
    # print v
    for sub_index in date_index:
        nums_1 = []
        nums_2 = []
        for i in sub_index:
            nums_1.append(n[i[0]][i[1]])
            nums_2.append(v[i[0]][i[1]])
        date_nums.append(nums_1)
        date_nums.append(nums_2)
    # print date_nums

    date_nums_2 = []
    for i in range(width):
        nums = []
        for y in range(width):
            nums.append(n[y][i])
        date_nums_2.append(nums)
    # print date_nums_2

    return date_nums+date_nums_2+data

find_position(d)

print checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ])