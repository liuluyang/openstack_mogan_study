#coding:utf8
import datetime
def checkio(year):

    result = [i for i in range(1,13) if datetime.datetime(year,i,13).weekday()==4]

    return len(result)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(2015) == 3, "First - 2015"
    assert checkio(1986) == 1, "Second - 1986"
