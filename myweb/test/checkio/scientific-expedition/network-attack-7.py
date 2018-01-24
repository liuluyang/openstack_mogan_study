#codinig:utf8


def checkio(nums):
    levels = {}
    width = len(nums)
    for i in range(width):
        levels[i]=nums[i][i]
    print levels

    links = []
    for i in range(width):
        for y in range(width):
            if  y>i and nums[i][y]==nums[y][i]==1:
                links.append(set([i,y]))
    print links


checkio([[0, 1, 0, 1, 0, 1],
         [1, 1, 1, 0, 0, 0],
         [0, 1, 2, 0, 0, 1],
         [1, 0, 0, 1, 1, 0],
         [0, 0, 0, 1, 3, 1],
         [1, 0, 1, 0, 1, 2]]) #== 4
checkio([[0, 1, 1],
         [1, 9, 1],
         [1, 1, 9]]) #== 9