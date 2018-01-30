#coding:utf8


import copy
from itertools import groupby
def break_rings(rings):
    rings = list(rings)
    nums = [i for s in rings for i in s]
    #print nums
    nums = list(groupby(sorted(nums, key=nums.count, reverse=True)))
    print nums
    result = 0
    for num in nums:
        for ring in copy.deepcopy(rings):
            if num[0] in ring:
                rings.remove(ring)
        if not rings:
            break
        result+=1

    return result



print break_rings(({1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {4, 6}))

print break_rings(({5, 6}, {4, 5}, {3, 4}, {3, 2}, {2, 1}, {1, 6}))

# if __name__ == '__main__':
#     # These "asserts" using only for self-checking and not necessary for auto-testing
#     assert break_rings(({1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {4, 6})) == 3, "example"
#     assert break_rings(({1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4})) == 3, "All to all"
#     assert break_rings(({5, 6}, {4, 5}, {3, 4}, {3, 2}, {2, 1}, {1, 6})) == 3, "Chain"
#     assert break_rings(({8, 9}, {1, 9}, {1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {8, 7})) == 5, "Long chain"
