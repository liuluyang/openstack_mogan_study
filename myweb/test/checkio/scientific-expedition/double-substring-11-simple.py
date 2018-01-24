#coding:utf8

import re
def double_substring(text):
    """
        length of the longest substring that non-overlapping repeats more than once.
    """
    # your code here
    sub_str = set([text[i:i + n] for n in range(1, len(text)) for i in
                   range(len(text)) if len(text)/2>=len(text[i:i + n])])
    max_list = [len(re.findall(word,text)[0]) for word in sub_str if len(re.findall(word,text))>=2]
    print max_list
    return max(max_list)

print double_substring('aghtfghkofgh')
print double_substring('ababa')

# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert double_substring('aaaa') == 2, "First"
#     assert double_substring('abc') == 0, "Second"
#     assert double_substring('aghtfghkofgh') == 3, "Third"
#     print('"Run" is good. How is "Check"?')
