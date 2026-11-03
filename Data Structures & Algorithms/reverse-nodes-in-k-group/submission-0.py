# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# approach 1 - iterate through the linked list, sever after every k nodes and add to a list. then go through the list and reverse each one. then make each one's end point to the next's start. just use a flag to reverse the last piece or not. O(3n) time, O(n/k) space

# approach 2 - modifying in place with O(1) space and 1 pass. for each group we need the tail of the previous group first. then we need to track the head and the tail of the reversed group. then you need the head of the next group.

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        new_head = ListNode()
        new_head.next = head # new_head = [0 > 1]
        prev_left = new_head # prev_left = [0 > 1]
        right = new_head # right = 0
        for i in range(k):
            right = right.next # 1,2
            if not right:
                return head
        
        while right:
            i = 0   
            group_head = None
            cur_left = prev_left.next  # cur_left = [1]
            next_head = right.next  # next_left = [3]
            while i < k:    # 0, 1
                nxt = cur_left.next # nxt = 2, 3
                cur_left.next = group_head # 2 > 1 > None
                group_head = cur_left # group_head = 2
                cur_left = nxt # cur_left = 3
                i += 1
            
            new_prev_left = prev_left.next # new_prev_left = 1
            prev_left.next = group_head # 0>2>1>None
            prev_left = new_prev_left # prev_left = 1
            prev_left.next = next_head # 0>2>1>None
            right = next_head # right=4

            i = 0
            while right and i < k-1:
                right = right.next
                if not right:
                    return new_head.next
                i += 1
        
        return new_head.next
