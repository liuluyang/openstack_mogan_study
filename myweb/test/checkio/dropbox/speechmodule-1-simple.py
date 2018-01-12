# coding:utf8

'''
1 one
2 two
3 three
4 four
5 five
6 six
7 seven
8 eight
9 nine

10 ten
11 eleven
12 twelve
13 thirteen
14 fourteen
15 fifteen
16 sixteen
17 seventeen
18 eighteen
19 nineteen

20 twenty
30 thirty
40 forty
50 fifty
60 sixty
70 seventy
80 eighty
90 ninety

100 one hundred


1000 one thousand
'''

FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]

NUM_LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
            20, 30, 40, 50, 60, 70, 80, 90]
STR_LIST = FIRST_TEN + SECOND_TEN + OTHER_TENS
DICT = dict(zip(NUM_LIST, STR_LIST))


def checkio(num):
    results_list = []
    Hundreds = int(num / 100)
    Ten = int(num % 100 / 10)
    A_bit = int(num % 100 % 10)

    if Hundreds in DICT:
        results_list.extend([DICT[Hundreds], 'hundred'])
    if Ten >= 2:
        results_list.append(DICT[Ten * 10])
        if A_bit in DICT:
            results_list.append(DICT[A_bit])
    if Ten <= 1:
        try:
            results_list.append(DICT[Ten * 10 + A_bit])
        except:
            pass

    result_str = ' '.join(results_list)
    return result_str
print checkio(100)

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(
        ' '), "Don't forget strip whitespaces at the end of string"
