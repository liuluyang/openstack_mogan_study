#coding:utf8


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        2+2+3*4/5-4+6
        + + * / - +
        2 2 3 4 5 4 6
        """
        results = []
        num = 0
        sym = '+'
        for i in s+'+':
            if i.isdigit():
                num = num*10+int(i)
            elif i in '+-*/':
                if sym=='+':
                    results.append(num)
                if sym=='-':
                    results.append(-num)
                if sym=='*':
                    results.append(results.pop()*num)
                if sym=='/':
                    tmp = results.pop()
                    if tmp//num<0 and tmp%num!=0:
                        results.append(tmp//num+1)
                    else:
                        results.append(tmp//num)
                sym = i
                num = 0
        return sum(results)



s = Solution()
print s.calculate(" 33 + 2 * 2-1*2")
