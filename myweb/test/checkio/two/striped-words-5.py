#coding:utf8

'''
字母表包含元音和辅音字母（是的，我们分开字母）。
元音 - A E I O U Y
辅音 - B C D F G H J K L M N P Q R S T V W X Z

给你一个不同的文字块。 这些单词由空格和标点符号分隔。
在这个任务中，数字不被视为单词（字母和数字的混合也不是一个单词）。
你应该计算辅音元音交替的单词（条纹词）的数量， 你算的单词不能有两个连续的元音或辅音。
由单个字母组成的单词没有条纹 - 不计数。 这个任务并不重要。
'''

import re
def checkio(words):
    Y = 'aeiouy'
    F = 'bcdfghjklmnpqrstvwxz'
    words = re.split(',| |\.|\?|!|;|:',words.lower())
    word_list = [word for word in words if word.isalpha() and len(word)>1]
    num = 0
    for word in word_list:
        if set(word[::2]+Y)==set(Y) and set(word[1::2]+F)==set(F) or \
            set(word[1::2]+Y)==set(Y) and set(word[::2]+F)==set(F):
            num +=1
    return num




print checkio('To take a trivial example, which of us ever undertakes laborious physical '
              'exercise,except to obtain some advantage from it?')

vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
cons = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z'}
import re
def checkio(text):
    word_list = re.findall(r"([\w]{2,})+",text.lower())
    count = 0
    for word in word_list:
        count += 1 if set(word[::2]) <= vowels and set(word[1::2]) <= cons else 0
        count += 1 if set(word[1::2]) <= vowels and set(word[::2]) <= cons else 0
    return count

print checkio('To take a trivial example, which of us ever undertakes laborious physical '
              'exercise,except to obtain some advantage from it?')
