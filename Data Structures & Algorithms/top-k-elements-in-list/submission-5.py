# option 1: iterate through, keep track with heap of tuples of (count, number)?
# option 2: bucketsort
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        
        counts = [[] for _ in range(len(nums) + 1)]
        for key in d.keys():
            counts[d[key]].append(key)
        # print(counts)
        
        res = []
        ind = len(nums)
        while ind >= 0:
            while counts[ind] and len(res) < k:
                res.append(counts[ind].pop())
            ind -= 1
        return res
        
        # heap = []
        # for num in d.keys():
        #     heapq.heappush(heap, (d[num], num))
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        
        # return [num[1] for num in heap]