#coding:utf8
def T(v=None):
    t = 1
    if not v:
        t = 2
    return t

t = T()
print t

print 'é' in 'edēéěèêāáàūúǔùǖǘǚǜīíǐì'
print 'é' in 'ā á ǎ à ō ó ǒ ò ē é ě è ī í ǐ ì ū ú ǔ ù ǖ ǘ ǚ ǜ'
replace_dict = {'a':'ā á ǎ à','e':'ē é ě è','i':'ī í ǐ ì','o':'ō ó ǒ òö','u':'ū ú ǔ ù'}

print "À`"
print list("À`")
print u'\xe9',u'\u1ebd'
s2 = u"ãÃẽẼĩĨñÑõÕũŨṽṼỹỸ"
print list(s2)
s =  u"ờỜừỪA"
for i in list(s):
    print i