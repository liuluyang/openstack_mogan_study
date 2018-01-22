#coding:utf8

def reverse_roman(roman_string):
    A = ['I','II','III','IV','V','VI','VII','VIII','IX']
    B = ['X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
    C = ['C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
    D = ['M','MM','MMM']
    #replace this for solution
    result = 0
    for i,v in enumerate(D[::-1]):
        if roman_string.find(v)==0:
            result += (3-i)*1000
            roman_string = roman_string.replace(v,'')
    for i,v in enumerate(C[::-1]):
        if roman_string.find(v)==0:
            result += (9-i)*100
            roman_string = roman_string.replace(v,'')
    for i,v in enumerate(B[::-1]):
        if roman_string.find(v)==0:
            result += (9-i)*10
            roman_string = roman_string.replace(v,'')
    for i,v in enumerate(A[::-1]):
        if roman_string.find(v)==0:
            result += (9-i)
            roman_string = roman_string.replace(v,'')
    return result

print reverse_roman('CDXCIX')

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert reverse_roman('VI') == 6, '6'
    assert reverse_roman('LXXVI') == 76, '76'
    assert reverse_roman('CDXCIX') == 499, '499'
    assert reverse_roman('MMMDCCCLXXXVIII') == 3888, '3888'
    print('Great! It is time to Check your code!')