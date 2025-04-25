# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 中节点的处理逻辑
# 1. root.val<low：root.left都不符合条件
# 2. root.val>high：root.right都不符合条件

class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if root is None:
            return None
        # 中节点
        if root.val<low:
            return self.trimBST(root.right, low, high)
        elif root.val>high:
            return self.trimBST(root.left, low, high)
        # 左节点
        root.left=self.trimBST(root.left, low, high)
        # 右节点
        root.right=self.trimBST(root.right, low, high)

        return root