#coding:utf8


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        results = set([])
        for index,num in enumerate(candidates):
            if num < target:
                result = [[num, num, index]]
                while result:
                    r = []
                    for i in result:
                        for index2,j in enumerate(candidates[i[-1]+1:]):
                            sum_ = i[-2]
                            if sum_ + j == target:
                                results.add(tuple(i[0:-2] + [j]))
                            elif sum_ + j*2 <= target:
                                r.append(i[0:-2] + [j, sum_ + j,i[-1]+index2+1])
                    result = r
        if target in candidates:
            results.add((target,))
        return map(list,results)

s = Solution()
print s.combinationSum2([1,1,2,5,6,7,10],8)

print s.combinationSum2([1],1)