# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "null"
        return (
            f"{root.val},{self.serialize(root.left)},{self.serialize(root.right)}"
        )
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = iter(data.split(","))
        def _dfs():
            val = next(values)
            if val == "null":
                return None
            node = TreeNode(val)
            node.left = _dfs()
            node.right = _dfs()
            return node
        return _dfs()