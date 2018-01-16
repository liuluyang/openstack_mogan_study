#coding:utf8


def subnetworks(net, crushes):

    new_net = []
    for sub_con in net:
        sub = set(sub_con)-set(crushes)
        #print sub
        if sub:
            new_net.append(sub)
    all_nodes = set([y for i in new_net for y in i])
    #print new_net
    #print all_nodes
    sub_num = 0
    review_nodes = set()
    #print review_nodes
    while review_nodes!=all_nodes:
        sub_num+=1
        _len = 0
        sub_net = set([list(all_nodes-review_nodes)[0]])
        while _len < len(sub_net):
            #print 1
            _len = len(sub_net)
            for link in new_net:
                if link & sub_net:
                    sub_net.update(link)
        review_nodes.update(sub_net)
        pass

    return sub_num

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert subnetworks([
            ['A', 'B'],
            ['B', 'C'],
            ['C', 'D']
        ], ['B']) == 2, "First"
    assert subnetworks([
            ['A', 'B'],
            ['A', 'C'],
            ['A', 'D'],
            ['D', 'F']
        ], ['A']) == 3, "Second"
    assert subnetworks([
            ['A', 'B'],
            ['B', 'C'],
            ['C', 'D']
        ], ['C', 'D']) == 1, "Third"
    print('Done! Check button is waiting for you!')