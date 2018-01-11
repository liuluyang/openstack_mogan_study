class Friends:

    def __init__(self, connections):
        self.friends = []
        for connection in connections:
            self.friends.append(connection)


    def add(self, connection):
        if connection not in self.friends:
            self.friends.append(connection)
            return True
        return False


    def remove(self, connection):
        if connection in self.friends:
            self.friends.remove(connection)
            return True
        return False

    def names(self):
        names = set()
        for friend in self.friends:
            for name in friend:
                names.add(name)
        return names



    def connected(self, name):
        connected = set()
        for friend in self.friends:
            if friend & set([name]):
                connected.add((friend-set([name])).pop())
        return connected

f = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
print f.remove({'a','c'})
print f.remove({'a','c'})