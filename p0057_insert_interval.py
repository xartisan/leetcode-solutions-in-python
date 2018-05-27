# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        done = False
        rv = []
        
        for interval in intervals:
            if not done:
                done = True
                if newInterval.end < interval.start:
                    rv.append(newInterval)
                    rv.append(interval)
                elif newInterval.start <= interval.start:
                    newInterval.end = max(newInterval.end, interval.end)
                    rv.append(newInterval)
                elif newInterval.start <= interval.end:
                    interval.end = max(interval.end, newInterval.end)
                    rv.append(interval)
                else:
                    rv.append(interval)
                    done = False
            else:
                last_interval = rv[-1]
                if interval.start > last_interval.end:
                    rv.append(interval)
                else:
                    last_interval.end = max(last_interval.end, interval.end)
        if not done:
            rv.append(newInterval)
        return rv