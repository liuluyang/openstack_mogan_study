#coding:utf8

def checkio(text, str):
    try:
        text = list(text)
        text.remove(str)
        return text.index(str)+1
    except:
        return None

print checkio('sims', 's')