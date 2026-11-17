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

        valid = True

        def dfs(node) -> Tuple(int, int):
            nonlocal valid
            if not node:
                return (None, None)

            minLeft, maxLeft = dfs(node.left)
            minRight, maxRight = dfs(node.right)

            mins = [x for x in [minLeft, minRight] if x is not None]
            maxes = [x for x in [maxLeft, maxRight] if x is not None]
            
            if (maxLeft is not None and maxLeft >= node.val) or (minRight is not None and minRight <= node.val):
                valid = False
            
            return (min(mins + [node.val]), max(maxes + [node.val]))
        
        dfs(root)
        return valid
        

