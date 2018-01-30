# coding:utf8

import itertools

itertools.permutations([1, 2, 3, 4], 2)


def checkio(data):
    moderate = sum(data) / 2.0
    nums_list = []
    for i in range(1, len(data)):
        nums_list += itertools.permutations(data, i)

    print nums_list

    result = min([abs(sum(i) - moderate) * 2 for i in nums_list])

    return result


from itertools import chain, combinations


def checkio(data):
    return min(abs(sum(data) - sum(part) * 2) for part in chain.from_iterable(
            combinations(data, r) for r in range(len(data) + 1)))


print checkio([2, 5, 7, 9])


print list(itertools.combinations([1,2,3],2))
print list(itertools.permutations([1,2,3],2))
