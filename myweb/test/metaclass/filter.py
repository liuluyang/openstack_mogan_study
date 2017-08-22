#coding:utf8

import abc
sensitive_words_list = ['asshole', 'fuck', 'shit']

def detect_sensitive_words(string):
  '''检测敏感词汇'''
  words_detected = filter(lambda word: word in string.lower(), sensitive_words_list)

  if words_detected:
    raise NameError('Sensitive words {0} detected in the string "{1}".' \
      .format(
        ', '.join(map(lambda s: '"%s"' % s, words_detected)),
        string
      )
    )

class CleanerMeta(type):

  def __new__(cls, class_name, bases, attrs):
    print class_name, bases, attrs
    detect_sensitive_words(class_name) # 检查类名
    map(detect_sensitive_words, attrs.iterkeys()) # 检查属性名

    print "Well done! You are a polite coder!" # 如无异常，输出祝贺消息

    return super(CleanerMeta, cls).__new__(cls, class_name, bases, attrs)
    # 重要！这行一定不能漏！！这回调用内建的类构造器来构造类，否则定义好的类将会变成 None


class APIBase(object):

  __metaclass__ = CleanerMeta


class ImAGoodBoy(APIBase):

  a_polite_attribute = 1

# [Output] Well done! You are a polite coder!

class FucMyBoss(APIBase):

  pass

# [Output] NameError: Sensitive words "fuck" detected in the string "FuckMyBoss".

class PretendToBePolite(APIBase):

  def fuc_your_assole(self):
    pass