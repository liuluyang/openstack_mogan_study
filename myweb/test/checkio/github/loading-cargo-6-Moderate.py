#coding:utf8

def checkio(data):

    data = sorted(data, reverse=True)
    moderate = sum(data)/2.0
    print data
    print moderate
    if len(data)==1:
        return data[0]
    if len(data)==2:
        return data[0]-data[1]
    last = data.pop(0)
    if last>=moderate:
        return (last-moderate)*2

    result = 0
    diff = 0
    others = []
    for i in range(len(data)):
        start = last
        for num in data[i:]:
            if start+num==moderate:
                return 0
            if start+num<moderate:
                start+=num
            else:
                others.append(start+num)
        if start==last:
            last = data[i]
        if result<start<moderate:
            result = start
    print result
    print sorted(others)

    return min([(moderate-result)*2,(sorted(others)[0]-moderate)*2])

#print checkio([12, 30, 30, 32, 42, 49])
# print checkio([5, 8, 13, 27, 14])
# print checkio([5,5,6,5])
# print checkio([4,24])
print checkio([20,1,49,18,21,48,17,35,23,50])
#print checkio([11,19,28,21,20,43,47,7,17])
# These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == '__main__':
#     assert checkio([10, 10]) == 0, "1st example"
#     assert checkio([10]) == 10, "2nd example"
#     assert checkio([5, 8, 13, 27, 14]) == 3, "3rd example"
#     assert checkio([5, 5, 6, 5]) == 1, "4th example"
#     assert checkio([12, 30, 30, 32, 42, 49]) == 9, "5th example"
#     assert checkio([1, 1, 1, 3]) == 0, "6th example"
