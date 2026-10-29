# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# approach 1: iterate through list and calculate the length, then get to the node that is before the one to remove. use dummy node before.
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        
        node_to_remove = length - n
        dummy = ListNode(val=-1, next = head)
        cur = dummy

        for _ in range(node_to_remove):
            cur = cur.next
        
        temp = cur.next.next
        cur.next = temp

        return dummy.next
