#coding:utf8

import copy
test_data = {"data":{"name":"li","age":"12"},"others":{"size":"22","width":{}}}

def test(key_name, data, result):
    #key_name = [].append(data.keys()[0])
    for k,v in data.items():
        #key_name = [k]
        key_name_2 = copy.deepcopy(key_name)
        key_name_2.append(k)
        #print 'key)name',key_name
        if v and isinstance(v, dict):
            #key_name.append(k)
            test(key_name_2, v, result)
        else:
            #key_name.append(k)
            result.append(('/'.join(key_name_2), v if v else ''))
    return result
t = test([], {"data":{"name":"li","age":"12"}}, [])
print t


def checkio(data):
    results = []
    for k,v in data.items():
        results += test([], {k:v}, [])
    return dict(results)

print checkio(test_data)


