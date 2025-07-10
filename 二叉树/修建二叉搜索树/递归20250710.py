# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. root.val<low: root.left都不符合条件
# 2. root.val>high: root.right都不符合条件
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:

        if root is None:
            return None
        
        if root.val<low: # 其root.left都不符合条件
            return self.trimBST(root.right, low, high)
        elif root.val>high: # 其root.right都不符合条件
            return self.trimBST(root.left, low, high)
        
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)

        return root