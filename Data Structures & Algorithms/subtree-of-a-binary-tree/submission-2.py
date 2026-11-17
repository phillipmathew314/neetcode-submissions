# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(node1, node2) -> bool:
            if not node1 and not node2:
                return True
            elif node1 and node2 and node1.val == node2.val:
                return isSameTree(node1.left, node2.left) and isSameTree(node1.right, node2.right)
            else:
                return False
        
        if not root and not subRoot:
            return True
        elif not root and subRoot:
            return False
        if isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)