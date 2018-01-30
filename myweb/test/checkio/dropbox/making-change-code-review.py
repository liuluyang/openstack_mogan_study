#coding:utf8


def checkio(price, denominations):
    pr = [0]+[price+1]*price
    #print pr

    for c in denominations:
        for p in range(price-c+1):
            pr[p+c] = min(pr[p]+1, pr[p+c])
    return pr[-1] if pr[-1] != price+1 else None


print checkio(123456, [1,6,7,456,678])
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(8, [1, 3, 5]) == 2
    assert checkio(12, [1, 4, 5]) == 3
    print('Done')