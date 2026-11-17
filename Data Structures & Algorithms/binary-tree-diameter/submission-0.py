# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def maxDepth(node: Optional[TreeNode]) -> int:
            nonlocal diameter
            
            if not node:
                return 0
            
            maxDepthLeft = maxDepth(node.left) + 1 if node.left else 0
            maxDepthRight = maxDepth(node.right) + 1 if node.right else 0
            diameter = max(diameter, maxDepthLeft + maxDepthRight)

            return max(maxDepthLeft, maxDepthRight)
        
        maxDepth(root)
        
        return diameter
        