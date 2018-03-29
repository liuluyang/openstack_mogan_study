#coding:utf8

import json
class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        return type(json.loads(s))

s = Solution()
print s.deserialize("[123,[456,[789]]]")