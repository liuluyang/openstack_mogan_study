#coding:utf8

def merge_intervals(intervals):
    """
        Merge overlapped intervals.
    """
    # Your code here
    result = [intervals.pop(0)]
    for x,y in intervals:
        last = result[-1][-1]
        if last-x>=-1:
            result[-1] = (result[-1][0],y if y>=last else last)
        else:
            result.append((x,y))
    print result
    return result

merge_intervals([(1, 4), (2, 6), (8, 10), (12, 19)])

# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert merge_intervals([(1, 4), (2, 6), (8, 10), (12, 19)]) == [(1, 6), (8, 10), (12, 19)], "First"
#     assert merge_intervals([(1, 12), (2, 3), (4, 7)]) == [(1, 12)], "Second"
#     assert merge_intervals([(1, 5), (6, 10), (10, 15), (17, 20)]) == [(1, 15), (17, 20)], "Third"
#     print('Done! Go ahead and Check IT')

