"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# approach 1: iterate through and copy stuff to a map that goes from node to index. then when building the new one, first pass builds all the "next" nodes and puts them in an array, and second pass builds all the random ones and uses the map and array to point. O(n) space, O(n) time

# approach 2: iterate through and copy stuff to a map that goes from old node to new node. then iterate through and assign next and random based on the map.
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        d = {}
        cur = head
        while cur:
            d[cur] = Node(x=cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            new_node = d[cur]
            if cur.next:
                new_node.next = d[cur.next]
            else:
                new_node.next = None
            
            if cur.random:
                new_node.random = d[cur.random]
            else:
                new_node.random = None
            
            cur = cur.next

        return d[head]