#coding:utf8


def largest_histogram(nums):

    _max = 0
    for num in set(nums):
        r = 0
        for n in nums:
            if n>=num:
                r += num
                if r>=_max:
                    _max = r
            else:
                r = 0
    return _max

print largest_histogram([1,2,1,2,2,1])
print largest_histogram([3])
print largest_histogram([5,3])

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert largest_histogram([5]) == 5, "one is always the biggest"
    assert largest_histogram([5, 3]) == 6, "two are smallest X 2"
    assert largest_histogram([1, 1, 4, 1]) == 4, "vertical"
    assert largest_histogram([1, 1, 3, 1]) == 4, "horizontal"
    assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"
    print("Done! Go check it!")