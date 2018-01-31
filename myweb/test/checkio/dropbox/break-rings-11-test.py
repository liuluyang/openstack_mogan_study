#coding:utf8

import itertools
import copy
from itertools import groupby
import time

def checkio(data):
    print time.clock()
    nums = [i for n in data for i in n]
    print 'int nums:',nums
    print len(nums)==len(data)*2

    nums_set = set(nums)
    print 'set nums:',nums_set

    all_sort = itertools.permutations(nums_set, len(nums_set))
    print 'all sort:',all_sort

    result = 0
    results = set()

    for sub_sort in all_sort:
        data_copy = copy.deepcopy(data)
        for i,num in enumerate(sub_sort):
            if not data_copy:
                results.add(i)
                break
            for d in copy.deepcopy(data_copy):
                if num in d:
                    data_copy.remove(d)
    print time.clock()
    return results



data = [[3,4],[5,6],[2,7],[1,5],[2,6],[8,4],[1,7],[4,5],[9,5],[2,3],[8,2],[2,4],[9,6],[5,7],[3,6],[1,3]]
#print checkio(data)

# a,b,c,d = [2,5],[3,4,6],[1,7],[8,9]
# all_link = []
# for i in itertools.permutations(a,2):
#     for y in itertools.permutations(b,3):
#         for z in itertools.permutations(c,2):
#             for w in itertools.permutations(d,2):
#                 all_link.append(i+y+z+w)
#
# print len(all_link)
rings = data
nums = [i for s in rings for i in s]
print nums
nums = sorted([(n,len(list(v))) for n,v in groupby(sorted(nums))], key=lambda k:k[1], reverse=True)

print nums