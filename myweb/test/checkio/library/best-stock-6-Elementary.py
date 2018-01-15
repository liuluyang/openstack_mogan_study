#coding:utf8

def checkio(kwargs):

    _max_k = ''
    _max = 0
    for key, value in kwargs.items():
        if value >_max:
            _max = value
            _max_k = key
    return _max_k

print checkio({'name':11,'f':13})

def best_stock(data):
    return max(data, key=lambda key: data[key])

print best_stock({'name':11,'f':13})

if __name__ == '__main__':
    print("Example:")
    print(checkio({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    }))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert checkio({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    }) == 'ATX', "First"
    assert checkio({
        'CAC': 91.1,
        'ATX': 1.01,
        'TASI': 120.9
    }) == 'TASI', "Second"
    print("Coding complete? Click 'Check' to earn cool rewards!")