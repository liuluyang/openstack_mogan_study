#coding:utf8

def checkio(words):
    _counter = [(i, words.count(i)) for i in set(words)]
    return sorted(_counter, key=lambda k:k[1])[-1][0]