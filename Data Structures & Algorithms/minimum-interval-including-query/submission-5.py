class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        heap = []
        i = 0
        res = {}
        for query in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= query:
                start, end = intervals[i]
                heapq.heappush(heap, (end-start+1, start))
                i += 1
            while heap and heap[0][1] + heap[0][0] <= query:
                heapq.heappop(heap)
            res[query] = heap[0][0] if heap else -1
        return [res[q] for q in queries]
            
