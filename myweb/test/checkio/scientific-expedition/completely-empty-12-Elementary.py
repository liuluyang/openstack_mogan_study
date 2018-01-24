#coding:utf8

from collections import Iterable
def completely_empty(val):
    #print isinstance('sa',Iterable)
    t = True
    tt = True

    try:
        #print val
        for i in val:
            #print i
            pass
        #print val
    except:
        #print val,'val'
        tt = False
    # if val:
    #     print val,'y'
    if val or (isinstance(val, Iterable) or tt):
        print val,'dd'
    # else:
    #     print val,'n'

    if val and (isinstance(val, Iterable) or tt):
        #print val
        for y in val:
            print y==1,'check'
            if not completely_empty(y):
                t = False
    if (val or val==0) and not isinstance(val, Iterable) and not tt:
        t = False

    return t


#print completely_empty([1])
c = type('', (), {'__getitem__': ().__getitem__})()
#print isinstance(c, Iterable)
# for i in c:
#     print i
#print completely_empty(type('', (), {'__getitem__': ().__getitem__})())
print completely_empty([iter((1,))])
print '############'
for i in [iter((1,))]:
    print i == iter((1,))
    for y in i:
        print y
print [iter((1,))][0]== iter((1,))
# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert completely_empty([]) == True, "First"
#     assert completely_empty([1]) == False, "Second"
#     assert completely_empty([[]]) == True, "Third"
#     assert completely_empty([[],[]]) == True, "Forth"
#     assert completely_empty([[[]]]) == True, "Fifth"
#     assert completely_empty([[],[1]]) == False, "Sixth"
#     assert completely_empty([0]) == False, "[0]"
#     assert completely_empty(['']) == True
#     assert completely_empty([[],[{'':'No WAY'}]]) == True
#     print('Done')
print '&&&&&&&&&&&&&&'
def test(t):
    if t and isinstance(t,Iterable):
        print t
        for i in t:
            print i
            test(i)

print test([iter((1,))])

print '******************'
s = iter((1,2)) #每个元素只可迭代一次

for i in s:
    print i
    if i==1:
        break

for y in s:
    print y,'yyy'


#best solutions
# def completely_empty(val):
#     try:
#         val = list(val)
#         if len(val)>0:
#             return all([completely_empty(x) for x in val])
#         return True
#     except:
#         return False