#coding:utf8

def checkio(nums):
    squares = [
        [1,2,6,5,1],
        [2,3,7,6,2],
        [3,4,8,7,3],
        [5,6,10,9,5],
        [6,7,11,10,6],
        [7,8,12,11,7],
        [9,10,14,13,9],
        [10,11,15,14,10],
        [11,12,16,15,11],
        [1,2,3,7,11,10,9,5,1],
        [2,3,4,8,12,11,10,6,2],
        [5,6,7,11,15,14,13,9,5],
        [6,7,8,12,16,15,14,10,6],
        [1,2,3,4,8,12,16,15,14,13,9,5,1]
    ]
    n = 0
    nums = [set(i) for i in nums]
    for square in squares:
        is_square = True
        for i in range(len(square)-1):
            if set([square[i],square[i+1]]) not in nums:
                is_square = False
                break
        if is_square:
            n += 1
    return n

if __name__ == '__main__':
    assert (checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
                     [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
                     [10, 14], [12, 16], [14, 15], [15, 16]]) == 3), "First, from description"
    assert (checkio([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
                     [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
                     [9, 13], [10, 11], [12, 16], [13, 14], [14, 15], [15, 16]]) == 2), "Second, from description"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 6]]) == 1), "Third, one small square"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 9], [6, 10], [9, 10]]) == 0), "Fourth, it's not square"
    assert (checkio([[16, 15], [16, 12], [15, 11], [11, 10],
                     [10, 14], [14, 13], [13, 9]]) == 0), "Fifth, snake"