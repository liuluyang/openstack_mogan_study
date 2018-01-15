#coding:utf8

def checkio(nums):
    if nums:
        return sorted(nums)[-1]-sorted(nums)[0]
    return 0

