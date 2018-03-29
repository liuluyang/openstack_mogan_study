#coding:utf8


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        m_list = list(magazine)
        for i in ransomNote:
            try:
                m_list.remove(i)
            except:
                print i
                return False
        return True

s = Solution()
print s.canConstruct('aa','aab')