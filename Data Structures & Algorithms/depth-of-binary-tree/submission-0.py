# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def _max_depth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            return 1 + max(_max_depth(node.left), _max_depth(node.right))

        return _max_depth(root)