#coding:utf8

from itertools import groupby
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        new_chars = []
        for s,ss in groupby(chars):
            l = len(list(ss))
            if l>1:
                new_chars.append(s)
                new_chars.extend([i for i in str(l)])
            else:
                new_chars.append(s)

        chars[0:]=new_chars
        print chars
        return len(new_chars)

s = Solution()
print s.compress(['a','a','a'])