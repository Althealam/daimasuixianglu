# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 递归法
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0 
        left_value = 0
        if root.left is not None and root.left.left is None and root.left.right is None:
            left_value=root.left.val
        return left_value+self.sumOfLeftLeaves(root.left)+self.sumOfLeftLeaves(root.right)