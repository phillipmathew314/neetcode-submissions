class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevEnd = intervals[0][1]
        res = 0

        for i in range(1, len(intervals)):
            newStart, newEnd = intervals[i]
            if newStart < prevEnd:
                prevEnd = min(prevEnd, newEnd)
                res += 1
            else:
                prevEnd = newEnd
        
        return res