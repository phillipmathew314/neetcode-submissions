# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # does the path include this node or not?
        # either it includes the left alone, the right alone, the node with both (recalculate global max here), the node with one, or the node alone

        # if the node is negative, then it would be either left or right (or alone if no children)
        # recalculate global max if both left and right exist and both are positive
        # if its positive, return the max of node + left and node + right 
        res = float('-inf')
        def maxSum(node) -> int:
            nonlocal res
            if not node.left and not node.right:
                return node.val
            
            maxSumRight = maxSumLeft = None
            unconnectedMax = float('-inf')
            connectedMax = node.val

            if node.right:
                maxSumRight = maxSum(node.right)
                unconnectedMax = maxSumRight
                connectedMax = max(node.val + maxSumRight, connectedMax)
            
            if node.left:
                maxSumLeft = maxSum(node.left)
                unconnectedMax = max(unconnectedMax, maxSumLeft)
                connectedMax = max(node.val + maxSumLeft, connectedMax)
            
            if node.right and node.left:
                unconnectedMax = max(unconnectedMax, maxSumRight + node.val + maxSumLeft)

            res = max(res, unconnectedMax)
            return connectedMax
        
        ms = maxSum(root)
        return max(ms, res)
            