#coding:utf8


def checkio(text):
    result = ''
    bug_str = ''
    replace_dict = {'a':u'āáǎà','e':u'ēéěè','i':u'īíǐì','o':u'ōóǒòö','u':u'ūúǔù'}
    # for k,v in replace_dict.items():
    #     for s in v:
    #         print text, v
    #         text = text.replace(s,k)
    #print list(text)
    for s in list(text):
        for k,v in replace_dict.items():
            if s in v:
                s = k
        result += s

    return result


print checkio(u"préfèrent")


# if __name__ == '__main__':
#     assert checkio(u"préfèrent") == u"preferent"
#     assert checkio(u"loài trăn lớn") == u"loai tran lon"
#     print('Done')