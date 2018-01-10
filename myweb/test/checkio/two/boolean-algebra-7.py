#coding:utf8

def checkio(x,y,text):
    if text=='conjunction':
        return x and y
    if text=='disjunction':
        return x or y
    if text=='implication':
        return not x or y
    if text=='exclusive':
        return x^y
    if text=='equivalence':
        return x==y

