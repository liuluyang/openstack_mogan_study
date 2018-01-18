#coding:utf8
import copy

def most_crucial(net, users):
    sub_net = {}
    for user in users.keys():
        net_copy = copy.deepcopy(net)
        for i in net_copy:
            if user in i:
                i.remove(user)
        #print net_copy
        sub_net[user] = make_sub_net(net_copy)
    #print sub_net
    for k,v in sub_net.items():
        num = 0
        for sub in v:
            sub_num = 0
            for i in sub:
                sub_num += users[i]
            sub_num = sub_num**2
            num += sub_num
        sub_net[k] = num + users[k]
    #print sub_net
    min_num = min(sub_net.values())
    result = [k for k,v in sub_net.items() if v==min_num]
    return result


def make_sub_net(net):
    new_net = []
    while net:
        start = set(net.pop(0))
        net_for = copy.deepcopy(net)
        _len = 0
        while _len <len(start):
            _len = len(start)
            for i in net_for:
                if start&set(i):
                    #print i
                    start.update(i)
                    try:
                        net.remove(i)
                    except:
                        pass
        new_net.append(start)
    return new_net


print most_crucial([
            ['A', 'B'],
            ['B', 'C']
        ],{
            'A': 10,
            'B': 10,
            'C': 10
        })

# print make_sub_net([['A'], ['B'],['A','B']])

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_crucial([
            ['A', 'B'],
            ['B', 'C']
        ],{
            'A': 10,
            'B': 10,
            'C': 10
        }) == ['B'], 'First'

    assert most_crucial([
            ['A', 'B']
        ],{
            'A': 20,
            'B': 10
        }) == ['A'], 'Second'

    assert most_crucial([
            ['A', 'B'],
            ['A', 'C'],
            ['A', 'D'],
            ['A', 'E']
        ],{
            'A': 0,
            'B': 10,
            'C': 10,
            'D': 10,
            'E': 10
        }) == ['A'], 'Third'

    assert most_crucial([
            ['A', 'B'],
            ['B', 'C'],
            ['C', 'D']
        ],{
            'A': 10,
            'B': 20,
            'C': 10,
            'D': 20
        }) == ['B'], 'Forth'

    print('Nobody expected that, but you did it! It is time to share it!')