# option 1: iterate through, keep track with heap of tuples of (count, number)?
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        
        heap = []
        for num in d.keys():
            heapq.heappush(heap, (d[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num[1] for num in heap]