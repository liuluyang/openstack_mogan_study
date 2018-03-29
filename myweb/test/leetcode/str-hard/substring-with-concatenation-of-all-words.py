#coding:utf8
import copy
class Solution(object):
    def _findSubstring(self, l, r, n, k, t, s, req, ans):
        curr = {}
        while r + k <= n:
            w = s[r:r + k]
            r += k
            if w not in req:
                l = r
                curr.clear()
            else:
                curr[w] = curr[w] + 1 if w in curr else 1
                while curr[w] > req[w]:
                    curr[s[l:l + k]] -= 1
                    l += k
                if r - l == t:
                    ans.append(l)

    def findSubstring(self, s, words):
        # if not s or not words or not words[0]:
        #     return []
        # n = len(s)
        # k = len(words[0])
        # t = len(words) * k
        # req = {}
        # for w in words:
        #     req[w] = req[w] + 1 if w in req else 1
        # ans = []
        # for i in xrange(min(k, n - t + 1)):
        #     print i
        #     self._findSubstring(i, i, n, k, t, s, req, ans)
        # return ans

        # s_len = len(s)
        # words = sorted(words)
        # print words
        # words_len = len(words)
        # word_len = len(words[0])
        # n = words_len*word_len
        # result = []
        # for i in range(s_len-n+1):
        #     print i,self.make_new(s[i:i+n],words_len,word_len)
        #     if s[i:i+word_len] in words:
        #         if self.make_new(s[i:i+n],words_len,word_len)==words:
        #             result.append(i)
        # return result

        def make_dict(s,word_len,words_num,check):
            index = 0
            for i in range(words_num):
                w = s[index:index+word_len]
                if w in check and check[w]>0:
                    check[w]-=1
                else:
                    return False
                index+=word_len
            return True
        word_len = len(words[0])
        words_num = len(words)
        words_len = word_len*words_num
        check = {}
        result = []
        for w in words:
             check[w] = check[w] + 1 if w in check else 1
        for i in xrange(len(s)-words_len+1):
            if s[i:i+word_len] in check:
                if make_dict(s[i:words_len+i],word_len,words_num,copy.deepcopy(check)):
                    result.append(i)
        return result

    def make_new(self,s,words,word_len):
        ans = []
        n = 0
        for i in range(words):
            ans.append(s[n:n+word_len])
            n+=word_len
        return sorted(ans)
s = Solution()
print s.findSubstring("barfoofoobarthefoobarman",["bar","foo","the"])
#print s.make_new('barfoofoo',3,3)

print s.findSubstring("wordgoodgoodgoodbestword",["word","good","best","good"])

print s.findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake",["fooo","barr","wing","ding","wing"])