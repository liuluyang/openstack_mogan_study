#coding:utf8


'''
无限的猴子定理指出，一只猴子在打字机键盘上随意敲击键无限长的时间，
几乎肯定会打出一个给定的文本，比如John Wallis的完整作品，或者更可能是Dan Brown的小说。

让我们假设我们的猴子正在打字，打字和打字，并产生了各种各样的短文本段。
让我们试着检查他们是否合理的单词包含。

给你一些可能包含合理词汇的文字。您应该计算给定文本中包含多少个单词。一个词应该是完整的，
可能是其他词的一部分。文字信箱没有关系。单词用小写字母表示，不要重复。
如果一个单词出现在文本中多次，它应该只计算一次。
'''
def count_words(text, words):
    r = 0

    for i in words:
        if i in text.lower():
            r +=1

    return r

print count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"})

def count_words(text, words):
    return sum(w in text.lower() for w in words)

