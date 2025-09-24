# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        rob, not_rob = self.dfs(root)
        return max(rob, not_rob)
    
    def dfs(self, node):
        if not node:
            return (0, 0)
        left_rob, left_not_rob = self.dfs(node.left)
        right_rob, right_not_rob = self.dfs(node.right)
        not_rob = max(left_rob, left_not_rob)+max(right_rob, right_not_rob)
        rob = node.val+left_not_rob+right_not_rob
        return (rob, not_rob)
        