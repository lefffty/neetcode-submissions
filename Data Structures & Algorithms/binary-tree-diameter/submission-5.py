# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diameter(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left_height = height(node.left)
            right_height = height(node.right)
            sub = max(
                diameter(node.left),
                diameter(node.right)
            )
            return max(sub, left_height + right_height)

        def height(node: Optional[TreeNode]):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))

        return diameter(root)