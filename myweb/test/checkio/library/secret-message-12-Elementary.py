#coding:utf8

def checkio(text):
    r = ''
    for i in text:
        if i.isupper():
            r +=i
    return r

def find_message(text):
    """Find a secret message"""

    return ''.join([char for char in text if char.isupper()])