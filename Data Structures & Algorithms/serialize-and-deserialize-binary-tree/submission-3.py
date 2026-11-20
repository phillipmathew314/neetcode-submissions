# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # could do a BFS and comma-separate it. depending on the level, you add a certain number of nulls
        # 1,1,0|2,2,0|3,2,1|4,3,2|5,3,3
        if not root:
            return ""
        queue = deque([(root, 0, 0)])
        res = ""
        while queue:
            node, row, col =  queue.popleft()
            res += f"{node.val},{2**row+col}|"
            if node.left:
                queue.append((node.left, row+1, col*2))
            if node.right:
                queue.append((node.right, row+1, col*2+1))

        return res

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # construct a map of nodes, with the hypothetical position in the array as the map key. by default these will be distinct.
        # when adding a new node, if you mod by 2 and it's zero and // by 2 and >= 1, then you add it as left child. if you mod by 2 and it's 1 and // by 2 and >= 1, then it's a right child
        if not data:
            return None
        
        data = data.split("|")
        data.pop()
        data_map = {}
        for s in data:
            val, pos = s.split(",")
            pos = int(pos)
            data_map[pos] = TreeNode(val)
            if pos // 2 in data_map:
                if pos % 2 == 0:
                    data_map[pos // 2].left = data_map[pos]
                else:
                    data_map[pos // 2].right = data_map[pos]
        
        return data_map[1]

        

