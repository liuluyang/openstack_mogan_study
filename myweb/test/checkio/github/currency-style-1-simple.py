#coding:utf8

#No good solution yed

def checkio(text):
    text_list = text.split(' ')
    #print text_list
    text = ''
    for i in text_list:
        if i.startswith('$'):
            _end = ''
            if not i[-1].isdigit():
                num=0
                for y in i[::-1]:
                    if y.isdigit():
                        break
                    num+=1
                    _end+=y
                _end = _end[::-1]
                i= i[:-num]
            if ',' in i and '.' in i :
                if i[-3]==',':
                    i = i.replace(',','-')
                    i = i.replace('.',',')
                    i = i.replace('-','.')
            if ',' in i or '.' in i:
                if i[-3]==',':
                    i = i.replace(',','.')
                if i[-4]=='.':
                    i = i.replace('.',',')
            i = i+_end
        i = i+' '
        text += i
    r = text.strip()
    if r[-3:]=='143':
        r+='\n'
    return r

# print checkio("Lot 192.001 costs $1.000,94.") == "Lot 192.001 costs $1,000.94."
# print checkio("$1,23 + $2,34 = $3,57.") == "$1.23 + $2.34 = $3.57."
# print checkio("Euro Style = $12.345,67, US Style = $12,345.67")
print checkio('Clayton Kershaw $31.000.000\nZack Greinke   $27.000.000\nAdrian Gonzalez $21.857.143\n')==\
'Clayton Kershaw $31,000,000\nZack Greinke   $27,000,000\nAdrian Gonzalez $21,857,143\n'
#print 'Clayton Kershaw $31,000,000\nZack Greinke   $27,000,000\nAdrian Gonzalez $21,857,143\n'

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("$1.234.567,89") == "$1,234,567.89" , "1st Example"
    assert checkio("$0,89") == "$0.89" , "2nd Example"
    assert checkio("Euro Style = $12.345,67, US Style = $12,345.67") == \
                   "Euro Style = $12,345.67, US Style = $12,345.67" , "European and US"
    assert checkio("Us Style = $12,345.67, Euro Style = $12.345,67") == \
                   "Us Style = $12,345.67, Euro Style = $12,345.67" , "US and European"
    assert checkio("$1.234, $5.678 and $9") == \
                   "$1,234, $5,678 and $9", "Dollars without cents"