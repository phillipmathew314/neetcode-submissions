class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # make heap based on tasks. iterate through tasks, and keep track of a map of the last time we saw the task. then add to the heap and add 2
        # tasks.sort()
        heap = []
        seen = defaultdict(int)
        filled = 0
        for task in tasks:
            heapq.heappush(heap, (seen[task], task))
            seen[task] += n+1
        
        cycle = 0
        while heap:
            val, task = heap[0]
            if val <= cycle:
                heapq.heappop(heap)
            cycle += 1
        
        return cycle
            