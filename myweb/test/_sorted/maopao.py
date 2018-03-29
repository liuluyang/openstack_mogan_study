#coding:utf8


import random
import time
def mp(lists):
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists

print mp([3,1,2,6,8,5,2])

nums = range(1000)
random.shuffle(nums)
#print nums
t1 = time.clock()
mp(nums)
print time.clock()-t1