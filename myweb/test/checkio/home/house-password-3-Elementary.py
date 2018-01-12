#coding:utf8
'''
斯蒂芬和索菲亚对于一切都使用简单的密码，忘记了安全性。
请你帮助尼古拉开发一个密码安全检查模块。如果密码的长度大于或等于10个符号，
至少有一个数字，一个大写字母和一个小写字母，该密码将被视为足够强大。
密码只包含ASCII拉丁字母或数字。
'''
def checkio(data):
    import re
    #replace this for solution

    if len(data)>=10 and re.search('[0-9]+',data) and re.search('[a-z]+',data) and re.search('[A-Z]+',data):
        return True
    else:
        return False


#Some hints
#Just check all conditions

# checkio = lambda s: not(
#         len(s) < 10
#         or s.isdigit()
#         or s.isalpha()
#         or s.islower()
#         or s.isupper()
#     )


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")