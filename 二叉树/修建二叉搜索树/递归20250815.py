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
        
        # 单层递归的逻辑
        if root.val<low:
            # root节点小于low==>root.left小于low==>只考虑root.right
            return self.trimBST(root.right, low, high)
        
        if root.val>high:
            # root节点大于high==>root.right大于high==>只考虑root.left
            return self.trimBST(root.left, low, high)
        
        if low<=root.val<=high:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
            return root # 返回更新后的剪枝过的当前节点root