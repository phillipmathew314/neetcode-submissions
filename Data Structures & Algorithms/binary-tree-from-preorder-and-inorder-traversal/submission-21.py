# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}

        def buildSubTree(pre_start, pre_end, in_start, in_end):
            if pre_start >= pre_end or in_start >= in_end:
                return None

            root = TreeNode(preorder[pre_start])
            mid = inorder_map[preorder[pre_start]]
            root.left = buildSubTree(pre_start+1, pre_start+(mid-in_start)+1, in_start, mid)
            root.right = buildSubTree(pre_start+(mid-in_start)+1, pre_end, mid+1, in_end)

            return root
        
        return buildSubTree(0, len(preorder), 0, len(inorder))