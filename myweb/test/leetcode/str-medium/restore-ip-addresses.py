#coding:utf8
from copy import deepcopy


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        length = len(s)
        check = {0: [[""]], 1: [], 2: [], 3: [], 4: []}
        for step in range(1, 5):
            ips = check[step - 1]
            for ip in ips:
                index = sum([len(i) for i in ip])
                num = 0
                for n in s[index:]:
                    #ip_new = deepcopy(ip) #Take up a lot of time
                    num = num * 10 + int(n)

                    if num == 0:
                        #ip_new.append(str(num))
                        check[step].append(ip+[str(num)])
                        break
                    elif 0 < num <= 255:
                        if 4 - step <= length - index - len(str(num)) <= (
                                4 - step) * 3:
                            #ip_new.append(str(num))
                            check[step].append(ip+str(num))
                        else:
                            continue
                    else:
                        break
        result = []
        for i in check[4]:
            if sum([len(j) for j in i]) == length:
                result.append('.'.join(i[1:]))
        return result

s = Solution()
print s.restoreIpAddresses('255111')
