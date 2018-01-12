#coding:utf8

def checkio(nums):
    #{1,2,3,4,5,7,8,12} ==> [(1,5),(7,8),(12,12)]
    #{1,2,3,6,4,5} ==> [(1,6)]
    print nums
    nums = list(nums)
    num_list = []
    index_list = []
    for index, value in enumerate(nums):
        if index==0:
            index_list.append(value)
        elif nums[index]-nums[index-1]==1:
            index_list.append(value)
        else:
            num_list.append(index_list)
            index_list = []
            index_list.append(value)
        if index==len(nums)-1:     #可能会对末尾字符忘记处理  对可能发生的情况未考虑到
            num_list.append(index_list)

    return [(i[0],i[-1]) for i in num_list]

print checkio({1,2,3,6,7,12})
print checkio({1, 2, 3, 6, 7, 8, 4, 5})
#对代码做测试很重要