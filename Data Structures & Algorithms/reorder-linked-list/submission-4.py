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
        dummy_head = ListNode(next=head)
        # dummy_head.next = head
        fast = slow = dummy_head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        last = slow.next
        slow.next = None

        reverse = None
        while last:
            temp = last.next
            last.next = reverse
            reverse = last
            last = temp
        
        first = head
        second = reverse
        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next
