#codinig:utf8

import copy
def checkio(nums):
    levels = {}
    width = len(nums)
    for i in range(width):
        levels[i]=nums[i][i]

    links = []
    for i in range(width):
        for y in range(width):
            if  y>i and nums[i][y]==nums[y][i]==1:
                links.append(set([i,y]))

    checked = {0:0}
    n = 0
    while links:
        n+=1
        for k,v in copy.deepcopy(checked).items():
            for i in copy.deepcopy(links):
                if k == list(i)[0] and levels[list(i)[1]]+v==n:
                    checked[list(i)[1]]=n
                    links.remove(i)
        for k in copy.deepcopy(checked):
            for i in copy.deepcopy(links):
                if k==list(i)[1]:
                    links.remove(i)
    return n



print checkio([[0, 1, 0, 1, 0, 1],
         [1, 1, 1, 0, 0, 0],
         [0, 1, 2, 0, 0, 1],
         [1, 0, 0, 1, 1, 0],
         [0, 0, 0, 1, 3, 1],
         [1, 0, 1, 0, 1, 2]]) #== 4
print checkio([[0, 1, 1],
         [1, 9, 1],
         [1, 1, 9]]) #== 9