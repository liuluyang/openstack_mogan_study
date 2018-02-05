#coding:utf8


def get_cookie(cookie, name):
    cookie = cookie.split(';')
    for i in cookie:
        s = i.split('=')
        if s[0].strip()==name:
            return s[1]

    return ''


print get_cookie('theme=light; sessionToken=abc123', 'theme')

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert get_cookie('theme=light; sessionToken=abc123', 'theme') == 'light', 'theme=light'
    assert get_cookie('_ga=GA1.2.447610749.1465220820; _gat=1; ffo=true', 'ffo') == 'true', 'ffo=true'
    print("Looks like you know everything. It is time for 'Check'!")
