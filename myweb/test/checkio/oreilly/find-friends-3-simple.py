#coding:utf8

list_1 = ['sun','find']
list_2 = ['find','cat']
list_3 = ['cat','person']

print list_1+list_2

def check_connection(args,name1,name2):
    all_con = []
    for con in args:
        con_list = con.split('-')
        all_con.append(con_list)
    con_dict = {0:[name1]}
    _key = 0
    while True:
        con_dict[_key+1]=[]
        for name in con_dict[_key]:
            for name_pat in all_con:
                if name in name_pat:
                    name_pat.remove(name)
                    con_dict[_key+1].append(name_pat.pop())
        if not con_dict[_key+1]:
            break
        _key +=1
    for i in con_dict.values():
        if name2 in i:
            return True
    return False

print check_connection(
    ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
     "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    "scout2", "scout3")
print check_connection(
    ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
     "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    "dr101", "sscout")
