#coding:utf8



import collections
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # task_counts = collections.Counter(tasks).values()
        # print collections.Counter(tasks)
        # print task_counts
        # M = max(task_counts)
        # Mct = task_counts.count(M)
        # #return max(len(tasks), (M - 1) * (n + 1) + Mct)
        #
        # l = len(tasks)
        # if Mct-1>=n:
        #     return l
        # else:
        #     if l-Mct*M>=(n-(Mct-1))*(M-1):
        #         return l
        #     else:
        #         return (M - 1) * (n + 1) + Mct

        task_count = collections.Counter(tasks).values()
        Max = max(task_count)
        Max_num = task_count.count(Max)
        #return max(len(tasks),(Max-1)*(n+1)+Max_num)
        return max(len(tasks),Max*(n+1)-(n-(Max_num-1)))



s = Solution()
ss = 'aabb'
print s.leastInterval(list(ss),2)