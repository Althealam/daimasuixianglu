# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.compare(root.left, root.right)
    
    def compare(self, left, right):
        if left is None or right is None:
            return left is right
        return left.val==right.val and self.compare(left.left, right.right) and self.compare(left.right, right.left)
        