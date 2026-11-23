class MedianFinder:
    # initial approach: keep track of an array. addNum just adds the number in sorted order (insertion sort). findMedian is O(1) as it goes straight to the middle of the array. nlogn

    # alternative approach: keep two heaps, a max heap and a min heap. can get the median from top and bottom. the only thing is finding the right pivot and keeping both heaps equal size or within 1. this would be log(n/2) for each insert and O(1) for median
    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        self.count = 0

    def addNum(self, num: int) -> None:
        if not self.max_heap:
            # heapq.heappush_max(self.max_heap, num)
            self.max_heap.append(num)
        elif not self.min_heap:
            if num > self.max_heap[0]:
                # heapq.heappush(self.min_heap, num)
                self.min_heap.append(num)
            else:
                self.min_heap.append(self.max_heap[0])
                self.max_heap[0] = num
        else:
            pivot = self.max_heap[0]
            if num < pivot:
                if len(self.max_heap) > len(self.min_heap):
                    heapq.heappush(self.min_heap, heapq.heappop_max(self.max_heap))
                    heapq.heappush_max(self.max_heap, num)
                else:
                    heapq.heappush_max(self.max_heap, num)
            else:
                if len(self.max_heap) > len(self.min_heap):
                    heapq.heappush(self.min_heap, num)
                else:
                    if num < self.min_heap[0]:
                        heapq.heappush_max(self.max_heap, num)
                    else:
                        heapq.heappush_max(self.max_heap, heapq.heappop(self.min_heap))
                        heapq.heappush(self.min_heap, num)
                    
        self.count += 1

    def findMedian(self) -> float:
        # print(self.max_heap, self.min_heap)
        if self.count and self.count % 2 == 0:
            return (self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return self.max_heap[0]
        