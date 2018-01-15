#coding:utf8


def checkio(text, begin, end):

    if begin in text and end not in text:
        return text.split(begin, 1)[-1]
    elif begin not in text and end in text:
        return text.split(end, 1)[0]
    elif begin in text and end in text:
        r = (text.split(begin, 1)[-1]).split(end, 1)
        if len(r)!=2:
            return ''
        else:
            return r[0]
    else:
        return text

def between_markers(text, begin, end):
    start = text.find(begin)
    finish= text.find(end)

    finish= None if finish==-1 else finish
    start= None if start==-1 else start+len(begin)

    return text[start:finish]

print between_markers('No <hi>', 'N', '<')
    
if __name__ == '__main__':
    print('Example:')
    print(checkio('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert checkio('What is >apple<', '>', '<') == "apple", "One sym"
    assert checkio("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert checkio('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert checkio('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert checkio('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert checkio('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')