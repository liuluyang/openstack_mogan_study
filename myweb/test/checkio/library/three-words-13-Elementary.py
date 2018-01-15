#coding:utf8


def checkio(text):
    num = 0
    for i in text.split(' '):
        if i.isalpha():
            num +=1
            if num>=3:
                return True
        else:
            num = 0
    return False