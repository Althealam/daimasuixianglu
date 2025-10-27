# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. get the height of the tree
# 2. judge whether the height difference of left and right>1, if yes then it is not a balanced binary tree
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        h = abs(self.get_height(root.left)-self.get_height(root.right))
        if h<=1: # the main difference between root.left and root.right is qualified
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False
    
    def get_height(self, root):
        if not root:
            return 0
        return max(self.get_height(root.left), self.get_height(root.right))+1