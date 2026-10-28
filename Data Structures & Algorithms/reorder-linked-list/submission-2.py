# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# approach 1: O(n) mem, O(n) runtime: put it all in an array and iterate in new order
# approach 2: O(n) mem, O(n) runtime: make copy of reversed linked list, and iterate through both linked lists
# approach 3: O(1) mem, O(n^2) runtime: iterate twice through the list to get first and last elements each time, and pop them both
# approach 4: O(1) mem, O(n) runtime: iterate through once to find the length. then iterate to the midpoint, and from the midpoint onwards, reverse the list. then iterate through both heads to get the new list
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head and not head.next:
            return
        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        midpoint = length // 2

        node = head
        ind = 0
        while ind < midpoint:
            node = node.next
            ind += 1

        reversed_head = self.reverseList(node)
        res = ListNode()
        res.next = head
        cur = head
        even = False
        while head and reversed_head:
            if even:
                temp = cur.next
                cur.next = head
                reversed_head = temp
                head = head.next
                even = False
            else:
                temp = cur.next
                cur.next = reversed_head
                head = temp
                reversed_head = reversed_head.next
                even = True
            cur = cur.next

        head = res
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        dummy = ListNode()
        dummy.next = head
        temp = head.next
        head.next = None
        head = temp

        while head:
            temp_head = head.next
            temp_next = dummy.next
            dummy.next = head
            head.next = temp_next
            
            head = temp_head
        
        return dummy.next




