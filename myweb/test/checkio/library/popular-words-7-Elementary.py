#coding:utf8

def checkio(text, words):
    text = text.lower()
    _dict = {}
    for i in words:
        _dict[i] = text.count(i)
    return _dict

def checkio2(text, words):

    return dict([(i, text.lower().count(i)) for i in words])


