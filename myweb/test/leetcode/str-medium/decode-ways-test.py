#coding:utf8



class Solution():
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        #dp[i] = dp[i-1] if s[i] != "0"
        #       +dp[i-2] if "09" < s[i-1:i+1] < "27"
        # if s == "": return 0
        dp = [0 for x in range(len(s)+1)]
        dp[0] = 1
        #print dp
        for i in range(1, len(s)+1):
            if s[i-1] != "0":
                dp[i] += dp[i-1]
                #print dp,1
            if i != 1 and s[i-2:i] < "27" and s[i-2:i] > "09":  #"01"ways = 0
                dp[i] += dp[i-2]
        print dp
        return dp[len(s)]

        # length = len(s)
        # if length==0 or s[0]==0:
        #     return ''
        # check = [0]
        # result = 0
        # while check:
        #     index = check.pop(0)
        #     for i in range(2):
        #         if index+1==length:
        #             if s[index]!='0':
        #                 result+=1
        #             else:
        #                 result-=1
        #                 break
        #         else:
        #             check.append(index+1)
        #         if index+2==length:
        #             num = s[index:index+2]
        #             if '09'<num<'27':
        #                 result+=1
        #             elif num<='09':
        #                 result-=1
        #             elif num in ['30','40','50','60','70','80','90']:
        #                 return ''
        #         else:
        #             check.append(index+2)
        # print result


s = Solution()
print s.numDecodings('1212232121202324')

class Solution2(object):
    def numDecodings(self,nums):
        if not nums or nums[0] == '0':
            return 0

        def t(nums, i, temp):
            if i <= 0:
                return 1
            if nums[i] != '0':
                if i-1 in temp:
                    a = temp[i-1]
                else:
                    a = t(nums, i - 1,temp)
                    temp[i-1]=a
            else:
                a = 0
            if '09' < nums[i - 1:i + 1] < '27':
                if i-2 in temp:
                    b = temp[i-2]
                else:
                    b = t(nums, i - 2,temp)
                    temp[i-2]=b
            else:
                b = 0
            return a + b

        return t(nums, len(nums) - 1, {})

s = Solution2()
print s.numDecodings('1212232121202324')


class Solution3(object):
    def numDecodings(self,nums):
        if not nums or nums[0]=='0':
            return 0
        result = [1,1]
        for i in xrange(1,len(nums)):
            a = 0
            if nums[i]!='0':
                a+=result[-1]
            if '09'<nums[i-1:i+1]<'27':
                a+=result[-2]
            if a==0:
                return 0
            result.append(a)
        return result[-1]

s = Solution3()
print s.numDecodings('1212232121202324')
