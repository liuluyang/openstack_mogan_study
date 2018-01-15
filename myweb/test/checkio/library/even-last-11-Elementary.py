#coding:utf8

def checkio(nums):
    if nums:
        return int(sum(nums[0::2])*nums[-1])
    return 0