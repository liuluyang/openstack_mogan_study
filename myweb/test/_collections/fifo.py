from collections import OrderedDict

class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        if not isinstance(capacity,int) or capacity <= 0:
            raise ValueError
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)


new_dict = LastUpdatedOrderedDict(1)
new_dict['k'] = 1
new_dict['l'] = 2
new_dict['p'] = 4
new_dict['p'] = 2
print new_dict
