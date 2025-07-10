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
        if not root:
            return None

        # 处理头节点
        while root and (root.val<low or root.val>high):
            if root.val<low:
                root = root.right
            elif root.val>high:
                root = root.left
        
        # 处理左子树
        cur = root
        while cur:
            while cur.left and (cur.left.val<low or cur.left.val>high):
                cur.left = cur.left.right
            cur = cur.left # 继续处理左子树
        
        cur = root
        while cur:
            while cur.right and (cur.right.val<low or cur.right.val>high):
                cur.right = cur.right.left
            cur = cur.right
        
        return root

