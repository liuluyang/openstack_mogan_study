

class Node(object):
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def __repr__(self):
        return str(self.id)



node_states = [Node('aggre_1',1),Node('aggre_1',2),
               Node('aggre_2',3),Node('aggre_2',4),Node('aggre_2',5),
               Node('aggre_3',6),Node('aggre_3',7)]

print set(node_states)
def filter(nodes, num):
    def retry(nodes, num):
        node_list = set()
        filter_str = nodes[0].name
        node_list.add(nodes[0])
        nodes.pop(0)
        for obj in nodes:
            print obj.id,obj.name
            if obj.name == filter_str:
                node_list.add(obj)
                #nodes.remove(obj)
            if len(node_list)>=num:
                return node_list
        for i in node_list:
            try:
                nodes.remove(i)
            except:
                pass
    for i in range(3):
        print "for num:",i,nodes
        node_list = retry(nodes, num)
        if node_list:
            return node_list
        if len(nodes) < num:
            return  "filter false!!!!!!!!!!!!!!!"
    return "retry num is done!!!!!!!!!!"

print filter(node_states, 3)

num_list = [1,2,3,4,5,6]
for num,key in enumerate(num_list):
    print "num:",num,"key:",key,"num_list:",num_list
    if key < 3:
        num_list.remove(key)
    print num_list




