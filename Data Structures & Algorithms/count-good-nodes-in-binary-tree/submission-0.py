# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def isGood(node, cur_max) -> int:
            if not node:
                return 0
            new_max = max(cur_max, node.val)
            good_nodes = isGood(node.left, new_max) + isGood(node.right, new_max)
            if node.val >= cur_max:
                return good_nodes + 1
            return good_nodes
        
        return isGood(root, -101)