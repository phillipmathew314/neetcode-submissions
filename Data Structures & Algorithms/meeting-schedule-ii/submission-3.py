"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) < 2:
            return len(intervals)

        starts, ends = [], []
        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)
        
        starts.sort()
        ends.sort()
        starti, endi = 1, 0
        res = 1
        while starti < len(intervals):
            if starts[starti] < ends[endi]:
                starti += 1
                res = max(starti-endi, res)
            else:
                endi += 1
        
        return res
