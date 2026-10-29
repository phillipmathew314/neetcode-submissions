"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# approach 1: iterate through and copy stuff to a map that goes from node to index. then when building the new one, first pass builds all the "next" nodes and puts them in an array, and second pass builds all the random ones and uses the map and array to point. O(n) space, O(n) time
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        d = {}
        ind = 0
        cur = head
        new_head = Node(x=head.val)
        new_cur = new_head
        node_arr = []
        
        while cur:
            d[cur] = ind

            if cur.next:
                new_cur.next = Node(x=cur.next.val)
            else:
                new_cur.next = None

            node_arr.append(new_cur)
            new_cur = new_cur.next

            ind += 1
            cur = cur.next

        cur = head
        new_cur = new_head
        while cur:
            rand_node = None
            if cur.random:
                rand_ind = d[cur.random]
                rand_node = node_arr[rand_ind]

            new_cur.random = rand_node
            cur = cur.next
            new_cur = new_cur.next
        
        return new_head