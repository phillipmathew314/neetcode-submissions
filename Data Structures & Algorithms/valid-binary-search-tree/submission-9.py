# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # INVARIANT:
        # max value of left side is less than root, or null
        # min value of right side is greater than root, or null

        # dfs function returns both max and min of each node

        def dfs(node, low_bound, high_bound) -> bool:
            if not node:
                return True
            
            if node.val <= low_bound or node.val >= high_bound:
                return False
            
            return dfs(node.left, low_bound, node.val) and dfs(node.right, node.val, high_bound)
        
        return dfs(root, float('-inf'), float('inf'))
        

