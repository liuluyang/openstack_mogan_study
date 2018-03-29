#coding:utf8


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return self.change_num(num1)*self.change_num(num2)

    def change_num(self,num):
        nums_dict = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,
                     '7':7,'8':8,'9':9}
        n = 0
        length = len(num)
        for index,i in enumerate(num):
            n+=nums_dict[i]*10**(length-index-1)
        #print type(n)
        return n

#print dict(zip(['1','2'],[1,2]))

s = Solution()
print s.change_num('123')
print s.multiply('1213','34')