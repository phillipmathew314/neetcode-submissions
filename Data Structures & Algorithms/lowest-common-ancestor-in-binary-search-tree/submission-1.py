# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lo, hi = p, q
        if p.val > q.val:
            lo, hi = q, p
        
        def lca(node: TreeNode) -> TreeNode:
            nonlocal lo, hi
            if node and lo.val <= node.val <= hi.val:
                return node
            elif node.val < lo.val:
                return lca(node.right)
            elif node.val > hi.val:
                return lca(node.left)
        
        return lca(root)
