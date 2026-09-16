# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node: Optional[TreeNode]):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))
        
        def balanceFactor(node: Optional[TreeNode]):
            if not node:
                return True
            
            left_height = height(node.left)
            right_height = height(node.right)

            if abs(right_height - left_height) > 1:
                return False

            return balanceFactor(node.left) and balanceFactor(node.right)

        return balanceFactor(root)