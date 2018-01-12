#coding:utf8

'''
有一只鸽子吃饲料 一分钟后飞来两个 一分钟后又飞来三个 ..
一只鸽子一分钟吃一份饲料
请问给出饲料数 求吃到至少一份完整饲料的鸽子数量
注：先到先吃

'''
def checkio(feed):
    #1+2+3+4+5...
    #1+3+6+10+15
    bird_list = [1]
    index = 2
    while True:
        bird_list.append(bird_list[-1]+index)
        index +=1
        if sum(bird_list)>feed:
            break
    return bird_list[-2]

print checkio(1) == 1
print checkio(2) == 1
print checkio(5) == 3
print checkio(10) == 6