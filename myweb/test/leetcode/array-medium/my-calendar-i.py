#coding:utf8


class MyCalendar(object):

    def __init__(self):
        self.check = []
        self.min_num = -1
        self.max_num = -1
    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if start>=self.max_num:
            self.check.append((end,start))
            self.max_num = end
        elif end<=self.min_num:
            self.check.insert(0,(end,start))
            self.min_num = start
        else:
            for index,i in enumerate(self.check):
                if start<i[0]:
                    if end>i[-1]:
                        return False
                    else:
                        self.check.insert(index,(end,start))
                        break
        return True


