# coding:utf8

import string

'''
问题：
给你一个其中包含不同的英文字母和标点符号的文本，你要找到其中出现最多的字母，
返回的字母必须是小写形式，
当检查最想要的字母时，不区分大小写，所以在你的搜索中 "A" == "a"。
请确保你不计算标点符号，数字和空格，只计算字母。
如果你找到 两个或两个以上的具有相同的频率的字母， 返回那个先出现在字母表中的字母。
例如 -- “one”包含“o”，“n”，“e”每个字母一次，因此我们选择“e”。
'''


def checkio(text):
    text = text.lower()
    ABC = 'abcdefghijklmnopqrstuvwxyz'
    text_dict = {}
    text_list = []
    max_num = 0
    for i in text:
        if i.isalpha():
            if i in text_dict:
                text_dict[i] += 1
            else:
                text_dict[i] = 1
    print text_dict
    for k, v in text_dict.items():
        if v == max_num:
            text_list.append(k)
            max_num = v
        if v > max_num:
            text_list = []
            text_list.append(k)
            max_num = v
    print text_list
    text_list.sort()
    print text_list
    return text_list[0]


print checkio('ff234-,, asfdsasda')

#best solutions
def checkio(text):
    """
    We iterate through latyn alphabet and count each letter in the text.
    Then 'max' selects the most frequent letter.
    For the case when we have several equal letter,
    'max' selects the first from they.
    """
    text = text.lower()
    return max(string.ascii_lowercase, key=text.count)


print checkio('ff234-,, asfdsasda')
