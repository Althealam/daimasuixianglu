# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 时间复杂度：O(n)
# 空间复杂度：O(n)
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        targetSum-=root.val
        if root.left is None and root.right is None:
            return targetSum==0
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)