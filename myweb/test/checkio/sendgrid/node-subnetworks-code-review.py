#coding:utf8

def subnetworks(net, crushes):
    one_cities = []
    mult_cities = []

    for x in net:
        for y in crushes:
            if y in x:
                x.remove(y)
        if len(x) == 1:
            one_cities.append(x[0])
        elif len(x) > 1:
            mult_cities.append(x)

    return len(mult_cities) + \
        len([x for x in one_cities if x not in sum(mult_cities, [])])


if __name__ == '__main__':
    assert subnetworks([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D']
    ], ['B']) == 2, 'First'
    assert subnetworks([
        ['A', 'B'],
        ['A', 'C'],
        ['A', 'D'],
        ['D', 'F']
    ], ['A']) == 3, 'Second'
    assert subnetworks([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D']
    ], ['C', 'D']) == 1, 'Third'

    print('Done! Check button is waiting for you!')