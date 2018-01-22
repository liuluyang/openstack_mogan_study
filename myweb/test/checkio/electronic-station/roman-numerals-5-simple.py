#coding:utf8

def checkio(data):

    #replace this for solution
    A = ['I','II','III','IV','V','VI','VII','VIII','IX']
    B = ['X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
    C = ['C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
    D = ['M','MM','MMM']
    result = ''
    d = data/1000
    c = data%1000/100
    b = data%1000%100/10
    a = data%1000%100%10
    #print d,c,b,a
    if d>=1:
        result += D[int(d-1)]
    if c>=1:
        result += C[int(c-1)]
    if b>=1:
        result += B[int(b-1)]
    if a>=1:
        result += A[int(a-1)]
    return result

print checkio(2387)

# def checkio(data):
#     roman = (('M',  1000),
#               ('CM', 900),
#               ('D',  500),
#               ('CD', 400),
#               ('C',  100),
#               ('XC', 90),
#               ('L',  50),
#               ('XL', 40),
#               ('X',  10),
#               ('IX', 9),
#               ('V',  5),
#               ('IV', 4),
#               ('I',  1))
#
#     roman_numeral = ""
#     for roman, value in roman:
#         while data >= value:
#             data -= value
#             roman_numeral += roman
#
#     return roman_numeral

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'