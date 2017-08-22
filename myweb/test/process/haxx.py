import uuid

list_ = []
for i in range(10000):
    #list_.append(i)
    list_.append(uuid.uuid4().get_hex)
    if i==0:
        print type(uuid.uuid4().get_hex)
print list_
print len(list_)
print len(set(list_))