#coding:utf8

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        min_cost0, min_cost1 = cost[0], cost[1]
        #print min_cost0,min_cost1
        for c in cost[2:]:
            min_cost0, min_cost1 = min_cost1, min(min_cost0, min_cost1) + c
            print c
            print min_cost0,min_cost1
        #print min_cost0,min_cost1
        return min(min_cost0, min_cost1)



s = Solution()
print s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
# print s.minCostClimbingStairs([10, 15, 20])

