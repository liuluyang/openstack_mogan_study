#coding:utf8


class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        times = sorted([int(i[:2])*60+int(i[-2:]) for i in timePoints])
        print times
        length = len(times)
        if len(set(times))!=length:
            return 0
        mimitime = min(times[-1]-times[0],1440-(times[-1]-times[0]))
        for index in xrange(length-1):
            mimi = times[index+1]-times[index]
            if mimi<mimitime:
                mimitime = mimi

        return mimitime




s = Solution()

print s.findMinDifference(['12:22','13:43'])