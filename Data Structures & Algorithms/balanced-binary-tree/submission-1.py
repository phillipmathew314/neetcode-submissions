# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        balanced = True
        def depth(node: Optional[TreeNode]) -> int:
            nonlocal balanced

            if not node:
                return 0
            
            leftDepth = depth(node.left)
            rightDepth = depth(node.right)

            print(leftDepth, rightDepth, balanced)

            if abs(leftDepth - rightDepth) > 1:
                balanced = False
            
            return 1 + max(leftDepth, rightDepth)
        
        return abs(depth(root.left) - depth(root.right)) <= 1 and balanced