#coding:utf8


import copy
from itertools import groupby


import copy
from itertools import groupby
def break_rings(rings):
    rings = list(rings)
    result = 0
    while rings:
        nums = [i for s in rings for i in s]
        nums = list(groupby(sorted(nums, key=nums.count, reverse=True)))
        check = nums.pop(0)[0]
        for link in copy.deepcopy(rings):
            if check in link:
                rings.remove(link)
        result += 1

    return result



#print break_rings(({1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {4, 6}))

#print break_rings(({5, 6}, {4, 5}, {3, 4}, {3, 2}, {2, 1}, {1, 6}))

print break_rings([[1,7],[9,6],[3,6],[1,3]])
# if __name__ == '__main__':
#     # These "asserts" using only for self-checking and not necessary for auto-testing
#     assert break_rings(({1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {4, 6})) == 3, "example"
#     assert break_rings(({1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4})) == 3, "All to all"
#     assert break_rings(({5, 6}, {4, 5}, {3, 4}, {3, 2}, {2, 1}, {1, 6})) == 3, "Chain"
#     assert break_rings(({8, 9}, {1, 9}, {1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {8, 7})) == 5, "Long chain"


d = [3, 4, 5, 6, 2, 7, 1, 1, 5]
# g = groupby(d)
# ll = list(groupby(sorted(d, key=d.count, reverse=True)))
# print sorted(d, key=d.count, reverse=True)
long = [3, 4, 5, 6, 2, 7, 1, 5, 2, 6, 8, 4, 1, 7, 4, 5, 9, 5, 2, 3, 8, 2, 2, 4, 9, 6, 5, 7, 3, 6, 1, 3]
#
# print sorted(long, key=long.count, reverse=True)
# long.sort()
# print long
#print sorted(long, key=lambda k:k[0])
# import itertools
# p = itertools.permutations(set(d), len(set(d)))
# for i in p:
#     #print i
#     pass

# dd = {}
# for i in long:
#     if i in dd:
#         dd[i]+=1
#     else:
#         dd[i]=1
#
# print dd.items()
