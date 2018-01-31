#coding:utf8
from itertools import groupby

def make_next_num(data):
    rings = data
    nums = [i for s in rings for i in s]
    nums = sorted([(n,len(list(v))) for n,v in groupby(sorted(nums))], key=lambda k:k[1], reverse=True)
    #print nums
    if len(nums)==sum([n[1] for n in nums]):
        #print 1
        return [n[0] for n in nums]
    else:
        #print '>2'
        return [n[0] for n in nums if nums[0][1]>1]

#print make_next_num([[1,2],[2,3],[3,4],[4,5],[5,2],[1,6],[6,7],[7,8],[8,9],[9,6],[1,10],[10,11],[11,12],[12,13],[13,10],[1,14],[14,15],[15,16],[16,17],[17,14]])


#？当得到想要的结果时 如何及时停止 并返回结果
def check(data_dict,result):
    if data_dict['rings']:
        for n in data_dict['nums']:
            new_rings = [link for link in data_dict['rings'] if n not in link]
            new_dict = {'index':data_dict['index']+1,'nums':make_next_num(new_rings),'rings':new_rings}
            check(new_dict,result)
    else:
        print data_dict['index']
        result.add(data_dict['index'])
        # if result and result>data_dict['index'] or result==0:
        #     result = data_dict['index']
    #print result
    return result


def checkio(data):
    init_dict = {'nums':make_next_num(data),'index':0,'rings':data}
    print init_dict

    c = check(init_dict,set())
    #return c

data = [[3,4],[5,6],[2,7],[1,5],[2,6],[8,4],[1,7],[4,5],[9,5],[2,3],[8,2],[2,4],[9,6],[5,7],[3,6],[1,3]]
data2 = ({1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4})
print checkio(data)
#print checkio([[1,2],[2,3],[3,4],[4,5],[5,2],[1,6],[6,7],[7,8],[8,9],[9,6],[1,10],[10,11],[11,12],[12,13],[13,10],[1,14],[14,15],[15,16],[16,17],[17,14]])

def test(data):
    one = 2
    data = [link for link in data if one not in link]
    print make_next_num(data)

    one = 5
    data = [link for link in data if one not in link]
    print data #[[3, 4], [8, 4], [1, 7], [9, 6], [3, 6], [1, 3]]
    #经过验证 目前的求解逻辑不一定能得到正确结果
    #扩大过滤取值范围 只要不是单个连接数都要考虑进去
    print make_next_num(data)

#test(data)

