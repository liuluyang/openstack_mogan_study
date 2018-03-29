#coding:utf8

from itertools import cycle
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        def t(per,w_nums,ws_length,maxWidth):
            if w_nums>1:
                per.pop()
                ws_length-=1
                count = maxWidth-ws_length
                c = cycle(range(len(per)))
                while count:
                    index = c.next()
                    if per[index].isspace():
                        per[index]+=' '
                        count-=1
                return ''.join(per)
            else:
                per.pop()
                per.append(' '*(maxWidth+1-ws_length))
                return ''.join(per)
            pass
        result = []
        per = []
        w_nums = 0
        ws_length = 0
        for word in words:
            w_length = len(word)
            if ws_length+w_length<=maxWidth:
                per.append(word)
                per.append(' ')
                w_nums+=1
                ws_length+=w_length+1
            else:
                result.append(t(per,w_nums,ws_length,maxWidth))
                per = [word,' ']
                w_nums = 1
                ws_length = w_length+1
        per.pop()
        per.append(' '*(maxWidth+1-ws_length))
        result.append(''.join(per))
        return result

s = Solution()
print s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."],16)