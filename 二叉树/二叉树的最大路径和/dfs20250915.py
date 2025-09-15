# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf')
    
        def dfs(node):
            if node is None:
                return 0
            
            l_val = max(dfs(node.left), 0)
            r_val = max(dfs(node.right), 0)

            val = node.val+l_val+r_val

            nonlocal ans
            ans = max(ans, val)
            return max(l_val, r_val)+node.val
        dfs(root)
        return ans
        