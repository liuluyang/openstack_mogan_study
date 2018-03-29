#coding:utf8


class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        if '.' in IP:
            ip = IP.split('.')
        else:
            ip = IP.split(':')
        if len(ip)==4:
            for i in ip:
                if len(i)>=2 and i[0]=='0':
                    return "Neither"
                try:
                    num = int(i)
                except:
                    return "Neither"
                if num<0 or num>255:
                    return 'Neither'
            return 'IPv4'
        if len(ip)==8:
            for i in ip:
                try:
                    int(i,16)
                except:
                    return 'Neither'
            return 'IPv6'
        return 'Neither'

s = Solution()
print s.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334")