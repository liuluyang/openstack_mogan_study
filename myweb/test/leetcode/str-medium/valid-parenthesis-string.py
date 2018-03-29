#coding:utf8


class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # a = 0
        # b = 0
        # if s[-2:]=='(*':
        #     s = s[:-2]
        # s = list(s)
        # length = len(s)
        # if length==0:
        #     return True
        # if s[0]==')' or s[-1]=='(':
        #     return False
        # if length==1:
        #     if '*' in s:
        #         return True
        #     return False
        # else:
        #     for i in s:
        #         if i=='(':
        #             a+=1
        #             b+=1
        #         if i==')':
        #             a-=1
        #             b-=1
        #         if i=='*':
        #             a-=1
        #             b+=1
        #         if b<0:
        #             return False
        #     if a<=0<=b:
        #         return True
        #     return False

        a = 0
        b = 0
        for i in s[::-1]:
            if i==')':
                a-=1
                b-=1
            if i=='(':
                a+=1
                b+=1
            if i=='*':
                a-=1
                b+=1
            if b>0:
                b=0
            if a>0:
                return False

        if a<=0 and b==0:
            return True
        return False

s = Solution()
# print s.checkValidString('(*)')
#print s.checkValidString('(((*)')
# print s.checkValidString('(((**))**))*')
print s.checkValidString("(())((())()()(*)(*()(())())())()()((()())((()))(*")
print s.checkValidString('((*)(*))(((*)')
#print s.checkValidString('((*)(*))((*')
