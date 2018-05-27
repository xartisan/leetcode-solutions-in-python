# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x: x.start)
        rv = []

        for interval in intervals:
            if not rv or rv[-1].end < interval.start:
                rv.append(interval)
            else:
                last_interval = rv[-1]
                last_interval.end = max(last_interval.end, interval.end)
        return rv