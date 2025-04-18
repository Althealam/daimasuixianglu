
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        self.invertTree(root.left)
        root.left, root.right=root.right, root.left
        self.invertTree(root.left)
        return root