#coding:utf8
import copy
def checkio(price, denominations):
    """
        return the minimum number of coins that add up to the price
    """
    result = []
    for dex in range(len(denominations)):
        times = 0
        price_c = copy.deepcopy(price)
        good = 0
        for i in sorted(denominations,reverse=True)[dex:]:
            times += price_c/i
            #if times>=187:
                #print times
                #print 'price',price,i
            if price_c%i!=0:
                price_c = price_c%i
            else:
                good = 1
                break
        #print times,dex
        if good:
            result.append(times)

    if result and price/denominations[-1]>1:
        print 1
        for dex in range(1,price/denominations[-1]):
            times = dex
            price_c = copy.deepcopy(price-denominations[-1]*dex)
            good = 0
            for i in sorted(denominations,reverse=True)[1:]:
                times += price_c/i
                #if times>=187:
                    #print times
                    #print 'price',price,i
                if price_c%i!=0:
                    price_c = price_c%i
                else:
                    good = 1
                    break
            #print times,dex
            if good:
                result.append(times)

    return min(result) if result else None

print checkio(8, [1, 3, 5])
print checkio(123456, [1,6,7,456,678])

# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert checkio(8, [1, 3, 5]) == 2
#     assert checkio(12, [1, 4, 5]) == 3
#     print('Done')

