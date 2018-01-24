#coding:utf8

def checkio(timer):
    dia = ['....','...-','..-.','..--','.-..','.-.-',
           '.--.','.---','-...','-..-']
    time_list = timer.split(':')
    result = ''
    for i in time_list:
        if len(i)==1:
            i = '0'+i
        result += dia[int(i[0])][1:]
        result += ' '
        result += dia[int(i[1])]
        result += ' : '
    return result[1:-3]


print checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-"
print checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--."
print checkio("00:1:02") == ".. .... : ... ...- : ... ..-."
print checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-"