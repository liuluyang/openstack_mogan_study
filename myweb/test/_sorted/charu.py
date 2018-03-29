#coding:utf8

import random
import time
def cr(nums):
    pass


def insert_sort(lists):
    # 插入排序
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
            j -= 1
    return lists
#print insert_sort([14,2,1,4,6])
nums = range(5000)
random.shuffle(nums)
t1 = time.clock()
nums.sort()
print nums
print time.clock()-t1
