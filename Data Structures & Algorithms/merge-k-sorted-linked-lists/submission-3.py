import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        head = ListNode()
        cur = head

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
        
        while heap:
            val, ind = heapq.heappop(heap)
            cur.next = lists[ind]
            lists[ind] = lists[ind].next
            if lists[ind]:
                heapq.heappush(heap, (lists[ind].val, ind))
            
            cur = cur.next
        
        return head.next
