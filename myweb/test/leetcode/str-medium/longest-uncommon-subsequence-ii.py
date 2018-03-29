#coding:utf8



class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        #nums = set()
        # check = {}
        # checked = ''
        # for i in strs:
        #     length = len(i)
        #     if length not in check:
        #         check[length]=[i]
        #     else:
        #         check[length].append(i)
        #
        # for n in sorted(check.keys(), reverse=True):
        #     if len(set(check[n]))==len(check[n]):
        #         for s in check[n]:
        #             if s not in checked:
        #                 return n
        #     checked+='#'.join(check[n])+'#'
        # return -1

        # def issubsequence(s, t):
        #     t = iter(t)
        #     return all(c in t for c in s)
        #
        # for s in sorted(strs, key=len, reverse=True):
        #     if sum(issubsequence(s, t) for t in strs) == 1:
        #         return len(s)
        # return -1
        def issubsequence(s, t):
            start = 0
            for i in s:
                index = t[start:].find(i)
                if index != -1:
                    start += index + 1
                else:
                    return False
            return True
        strs = sorted(strs, key=len, reverse=True)
        check = set()
        for s  in strs:
            if s in check:
                continue
            check.add(s)
            l = len(s)
            num = 0
            for i in strs:
                if len(i)>=l:
                    if issubsequence(s,i):
                        num+=1
                else:
                    break
            if num==1:
                return l
        return -1
s = Solution()
print s.findLUSlength(['dsffsdf','dsffsdf','dsffsdf','ds','s','fsf','dsfffh'])


def issubsequence(s,t):
    start = 0
    for i in s:
        index = t[start:].find(i)
        if index!=-1:
            start +=index+1
        else:
            return False
    return True

print issubsequence('fsf','fshf')