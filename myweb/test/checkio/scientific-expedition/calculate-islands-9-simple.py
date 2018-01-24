#coding:utf8

import copy
def find_around(positions):
    arounds = []
    for position in positions:
        a = position[0]
        b = position[1]
        around = [
            (a,b+1),(a,b-1),
            (a+1,b),(a-1,b),
            (a+1,b+1),(a-1,b-1),
            (a+1,b-1),(a-1,b+1)
        ]
        arounds.extend(around)
    return arounds

def checkio(land_map):
    islands_position = [(x,y) for x,val in enumerate(land_map) for y,val2 in
                        enumerate(val) if land_map[x][y]==1]
    islands = []
    while islands_position:
        island = []
        _pop = islands_position.pop()
        island.append(_pop)
        ischeck = [_pop]
        while ischeck:
            check = copy.deepcopy(ischeck)
            ischeck = []
            for i in find_around(check):
                if i in islands_position:
                    ischeck.append(i)
                    island.append(i)
                    islands_position.remove(i)
        islands.append(island)


    return sorted([len(i) for i in islands])


print checkio([[0, 0, 0, 0, 0],
                [0, 0, 1, 1, 0],
                [0, 0, 0, 1, 0],
                [0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0]])
#These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == '__main__':
#     assert checkio([[0, 0, 0, 0, 0],
#                     [0, 0, 1, 1, 0],
#                     [0, 0, 0, 1, 0],
#                     [0, 1, 0, 0, 0],
#                     [0, 0, 0, 0, 0]]) == [1, 3], "1st example"
#     assert checkio([[0, 0, 0, 0, 0],
#                     [0, 0, 1, 1, 0],
#                     [0, 0, 0, 1, 0],
#                     [0, 1, 1, 0, 0]]) == [5], "2nd example"
#     assert checkio([[0, 0, 0, 0, 0, 0],
#                     [1, 0, 0, 1, 1, 1],
#                     [1, 0, 0, 0, 0, 0],
#                     [0, 0, 1, 1, 1, 0],
#                     [0, 0, 0, 0, 0, 0],
#                     [0, 1, 1, 1, 1, 0],
#                     [0, 0, 0, 0, 0, 0]]) == [2, 3, 3, 4], "3rd example"
