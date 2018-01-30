#coding:utf8


def count_neighbours(grid, row, col):
    positions = [(row,col+1),(row,col-1),
                 (row+1,col),(row-1,col),
                 (row+1,col+1),(row-1,col-1),
                 (row+1,col-1),(row-1,col+1)]
    result = 0
    for x,y in positions:
        if x>=0 and y>=0:
            try:
                result+=grid[x][y]
                #print (x,y)
            except:
                pass

    return result

print count_neighbours(((1, 1, 1),
                 (1, 1, 1),
                 (1, 1, 1),), 0, 2)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"
