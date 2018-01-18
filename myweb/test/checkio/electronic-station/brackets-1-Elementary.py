#coding:utf8

def checkio(expression):
    L = ['{','[','(']
    R = ['}',']',')']
    LR_list = []
    for s in expression:
        if s in L:
            LR_list.append(s)
        if s in R:
            if not LR_list or L[R.index(s)]!=LR_list[-1]:
                return False
            LR_list.pop()
    return True if not LR_list else False

#print checkio("((5+3)*2+1)")

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"