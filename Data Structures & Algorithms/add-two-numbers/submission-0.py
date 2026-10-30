# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# approach 1: iterate through both lists, construct numbers, use python addition, and construct solution
# approach 2. construct the list as you iterate through the lists and carry the tens
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0
        head = ListNode(val=0)
        node = head
        while l1 or l2:
            num = carry
            if l1:
                num += l1.val
                l1 = l1.next
            if l2:
                num += l2.val
                l2 = l2.next
            
            carry = num // 10
            digit = num % 10
            node.next = ListNode(val=digit)

            node = node.next
        
        if carry > 0:
            node.next = ListNode(val=carry)
        
        return head.next

