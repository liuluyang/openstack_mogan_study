#coding:utf8


def checkio(words):

    for word in words:
        for w in words:
            if word!=w and len(word)>=len(w) and w in word and word.split(w)[-1]=='':
                return True
    return False
assert checkio({"hello", "lo", "he"}) == True
assert checkio({"hello", "la", "hellow", "cow"}) == False
assert checkio({"walk", "duckwalk"}) == True
assert checkio({"one"}) == False
assert checkio({"helicopter", "li", "he"}) == False
