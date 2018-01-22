#coding:utf8

def checkio(num):
    num_list = []
    while True:
        nums = []
        for i in range(2,10):
            if num%i==0:
                nums.append(i)
        if nums:
            num = num/nums[-1]
            num_list.append(nums[-1])
            if num == 1:
                break
        else:
            num_list = []
            break

    num_list.sort()
    if num_list:
        return int(''.join([str(i) for i in num_list]))
    else:
        return 0
checkio(21)
