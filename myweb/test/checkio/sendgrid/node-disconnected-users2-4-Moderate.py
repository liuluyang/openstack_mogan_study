#coding:utf8
'''
#该题目虽然结果正确
但是对题目理解有错误

当一个节点出错 那么该节点跟外界的所有连接都会断开而不是部分断开
'''

def disconnected_users(net, users, source, crushes):

    con_dict = {0:[source]}
    _key = 0
    if source in crushes:
        return sum(users.values())
    while True:
        con_dict[_key+1]=[]
        for name in con_dict[_key]:
            for name_pat in net:
                if name in name_pat:
                    name_pat.remove(name)
                    pop_name = name_pat.pop()
                    if pop_name in crushes:
                        crushes.remove(pop_name)
                    else:
                        con_dict[_key+1].append(pop_name)
        if not con_dict[_key+1]:
            del con_dict[_key+1]
            break
        _key +=1
    #print con_dict
    connected_users = []
    for i in con_dict.values():
        connected_users.extend(i)
    others = set(users.keys())-set(connected_users)
    num = 0
    for i in others:
        num += users.get(i)
    return num

print disconnected_users([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D'],
    ['A','D']
    ], {
        'A': 10,
        'B': 20,
        'C': 30,
        'D': 40
    },
        'A', ['C'])

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert disconnected_users([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D']
    ], {
        'A': 10,
        'B': 20,
        'C': 30,
        'D': 40
    },
        'A', ['C']) == 70, "First"

    assert disconnected_users([
        ['A', 'B'],
        ['B', 'D'],
        ['A', 'C'],
        ['C', 'D']
    ], {
        'A': 10,
        'B': 0,
        'C': 0,
        'D': 40
    },
        'A', ['B']) == 0, "Second"

    assert disconnected_users([
        ['A', 'B'],
        ['A', 'C'],
        ['A', 'D'],
        ['A', 'E'],
        ['A', 'F']
    ], {
        'A': 10,
        'B': 10,
        'C': 10,
        'D': 10,
        'E': 10,
        'F': 10
    },
        'C', ['A']) == 50, "Third"

    print('Done. Try to check now. There are a lot of other tests')