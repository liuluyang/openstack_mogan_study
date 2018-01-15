#coding:utf8

import re

def first_word(text):
    numbers =  re.findall('[\w|\']+', text)
    print numbers
    return numbers[0]

#good solution
# def first_word(text):
#     word = re.search("[A-Za-z']+", text)
#     if word:
#         return word.group(0)

if __name__ == '__main__':

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("hello.world")



