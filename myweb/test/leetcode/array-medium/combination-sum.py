#coding:utf8


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        #print candidates
        cand_index = {}
        for index,num in enumerate(candidates):
            cand_index[num]=index
        #print cand_index
        results = []
        for num in candidates:
            if num<target:
                result = [[num,num]]
                while result:
                    r = []
                    for i in result:
                        for j in candidates[cand_index[i[-2]]:]:
                            sum_ = i[-1]
                            if sum_+j==target:
                                results.append(i[0:-1]+[j])
                            elif sum_+j*2<=target:
                                r.append(i[0:-1]+[j,sum_+j])
                    result = r
        if target in cand_index:
            results.append([target])
        return results

s = Solution()
print s.combinationSum([2, 3, 6,5,7],7)
print s.combinationSum([1,2],4)
print s.combinationSum([2,3,5],8)
print s.combinationSum([7,3,2],18)



