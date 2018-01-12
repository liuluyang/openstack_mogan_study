#coding:utf8

def checkio(text):
    if not text.endswith('.'):
        text += '.'
        text = text[0].upper()+text[1:]
    return text

print checkio('aafasd')
