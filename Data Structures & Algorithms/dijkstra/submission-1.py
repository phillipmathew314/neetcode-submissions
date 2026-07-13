class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        distMap = {}
        distMap[src] = 0
        adjList = {}
        for v in range(n):
            adjList[v] = []
            if v != src:
                distMap[v] = math.inf

        for u, v, w in edges:
            if u not in adjList:
                adjList[u] = [(v, w)]
            adjList[u].append((v, w))

        
        minHeap = [(0, src)]
        visited = set()

        while minHeap:
            curWeight, srcVertex = heapq.heappop(minHeap)
            if srcVertex in visited:
                continue
            curWeight = min(distMap[srcVertex], curWeight)

            for dstVertex, dstWeight in adjList[srcVertex]:
                newWeight = curWeight + dstWeight
                if newWeight < distMap[dstVertex]:
                    distMap[dstVertex] = newWeight
                if dstVertex not in visited:
                    heapq.heappush(minHeap, (newWeight, dstVertex))
                    
            visited.add(srcVertex)
        
        for key, val in distMap.items():
            if val == math.inf:
                distMap[key] = -1
        
        return distMap

