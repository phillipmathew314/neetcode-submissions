class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        res = []
        newStart, newEnd = newInterval
        placed = False
        for start, end in intervals:
            if placed or newStart > end:
                res.append([start, end])
            elif newEnd < start:
                res.append([newStart, newEnd])
                res.append([start, end])
                placed = True
            else:
                newStart = min(newStart, start)
                newEnd = max(newEnd, end)
        if not placed:
            res.append([newStart, newEnd])
        return res