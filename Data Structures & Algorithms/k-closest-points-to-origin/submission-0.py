class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # max heap is a tuple of (dist, point)
        heap = []
        for x, y in points:
            heapq.heappush_max(heap, ((x**2 + y**2)**0.5, (x, y)))
            if len(heap) > k:
                heapq.heappop_max(heap)
        
        for i, tup in enumerate(heap):
            _, point = tup
            x, y = point
            heap[i] = [x, y]
        return heap