# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_value = 0 # the answer
        # whether it is a left leaf node (the stop criterion)
        if root.left and root.left.left is None and root.left.right is None: # this is a left leaf node
            left_value+=root.left.val
        return left_value+self.sumOfLeftLeaves(root.left)+self.sumOfLeftLeaves(root.right) # recursion