#coding:utf8

class Friends(object):
    def __init__(self, connections):
        #connections = ({'a','b'},{'f','s'})
        self.connections = self.make_connections(connections)

    def make_connections(self, connections):
        conn = []
        for i in connections:
            if i not in conn:
                conn.append(i)
        return conn

    def add(self, connection):
        if connection not in self.connections:
            self.connections.append(connection)
            return True
        return False

    def remove(self, connection):
        if connection in self.connections:
            self.connections.remove(connection)
            return True
        return False

    def names(self):
        n = [y for i in self.connections for y in i]
        return set(n)

    def connected(self, name):
        if name in self.names():
            connected_list = []
            for i in self.connections:
                if name in i:
                    connected_list.extend(i)
            connected_list = set(connected_list)
            connected_list.remove(name)
            return connected_list
        return set()

f = Friends(({'a','b'},{'b','c'},{'b','a'}))
print f.connections
print f.add({'a','b'})
print f.add({'a','v'})

print f.names()
print f.connected('a')