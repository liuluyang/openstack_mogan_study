#coding:utf8



def disconnected_users(net, users, source, crushes):
    links = [{x, y} for x, y in net if x not in crushes and y not in crushes]
    print links
    connected_n = 0
    connected_nodes = {source} if source not in crushes else {}
    while connected_n < len(connected_nodes):
        print 1
        connected_n = len(connected_nodes)
        for link in links:
            if link & connected_nodes:
                connected_nodes.update(link)
        print connected_nodes
    print connected_nodes
    return sum(users[node] for node in set(users.keys()) - connected_nodes)


print disconnected_users([
    ['D','E'],
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D'],
    ['A','D'],
    #['D','E']
    ], {
        'A': 10,
        'B': 20,
        'C': 30,
        'D': 40
    },
        'A', ['C'])