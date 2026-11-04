class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # approach 1 - use max heap of k numbers, nlogk. have each element be a tuple of value and index. if index is not valid, keep popping until it is. (lazy but should be nlogk)
        # approach 2 (brute force) - find max of each window, n*k

        heap = []
        res = []

        for i in range(k):
            heapq.heappush_max(heap, (nums[i], i))
        res.append(heap[0][0])

        ind = k
        while ind < len(nums):
            heapq.heappush_max(heap, (nums[ind], ind))
            while heap[0][1] <= ind - k:
                heapq.heappop_max(heap)
            res.append(heap[0][0])
            ind += 1
        
        return res

