class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        curStart, curEnd = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            newStart, newEnd = intervals[i]
            if newStart > curEnd:
                res.append([curStart, curEnd])
                curStart, curEnd = newStart, newEnd
            else:
                curEnd = max(curEnd, newEnd)
        
        res.append([curStart, curEnd])
        return res