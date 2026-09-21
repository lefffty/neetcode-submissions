# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def _dfs(node: TreeNode, maxVal: int) -> int:
            if not node:
                return 0
            res = 1 if node.val >= maxVal else 0
            maxVal = max(node.val, maxVal)
            res += _dfs(node.left, maxVal)
            res += _dfs(node.right, maxVal)

            return res
        return _dfs(root, root.val)