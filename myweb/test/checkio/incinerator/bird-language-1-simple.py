#coding:utf8
import copy
VOWELS = "aeiouy"
ABC = "bcdfghjklmnpqrstvwxz"
def translate(phrase):
    for i in VOWELS:
        phrase = phrase.replace(i*3,i)
    #print phrase
    result = ''
    for i,s in enumerate(phrase):
        if s in ABC:
            result+=s
        elif s in VOWELS and phrase[i-1] in ABC:
            pass
        else:
            result+=s
    return result



print translate("hieeelalaooo")
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
