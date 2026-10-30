"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# approach 1: O(n) space, O(n) time - iterate through and copy stuff to a map that goes from node to index. then when building the new one, first pass builds all the "next" nodes and puts them in an array, and second pass builds all the random ones and uses the map and array to point. O(n) space, O(n) time

# approach 2: O(n) space, O(n) time - iterate through and copy stuff to a map that goes from old node to new node. then iterate through and assign next and random based on the map.

# approach 3: O(n) space, O(n) time - ONE PASS with hashmap

# approach 4...interleaving the new list into the old list

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # APPROACH 4
        cur = head

        while cur:
            new_node = Node(x=cur.val)

            temp = cur.next
            cur.next = new_node
            new_node.next = temp

            cur = cur.next.next
        
        cur = head
        while cur:
            new_node = None
            if cur.random:
                new_node = cur.random.next
            
            cur.next.random = new_node

            cur = cur.next.next
        
        cur = head
        new_head = Node(x=0)
        new_cur = new_head
        while cur:
            temp = cur.next
            cur.next = temp.next
            new_cur.next = temp

            new_cur = new_cur.next
            cur = cur.next
            
        return new_head.next

        # APPROACH 3
        # if not head:
        #     return None

        # cur = head
        # d = {cur: Node(x=head.val)}

        # while cur:
        #     new_node = d[cur]
        #     if cur.next:
        #         node = None
        #         if cur.next in d:
        #             node = d[cur.next]
        #         else:
        #             node = Node(x=cur.next.val)
        #             d[cur.next] = node
        #         new_node.next = node
        #     else:
        #         new_node.next = None

        #     if cur.random:
        #         node = None
        #         if cur.random in d:
        #             node = d[cur.random]
        #         else:
        #             node = Node(x=cur.random.val)
        #             d[cur.random] = node
        #         new_node.random = node
        #     else:
        #         new_node.random = None

        #     cur = cur.next

        # return d[head]