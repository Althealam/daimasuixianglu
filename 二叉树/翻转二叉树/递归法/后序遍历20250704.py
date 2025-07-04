# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 后序遍历，先翻转左右子节点，然后再翻转根节点
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root