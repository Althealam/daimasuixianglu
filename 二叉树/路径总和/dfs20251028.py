# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        res = []
        self.dfs(root, [], res, targetSum)
        if len(res)==0:
            return False
        return True
    
    def dfs(self, root, path, res, targetSum):
        if not root:
            return None
        path.append(root.val)
        if root.left is None and root.right is None and sum(path[:])==targetSum:
            res.append(path)
        if root.left:
            self.dfs(root.left, path, res, targetSum)
            path.pop()
        if root.right:
            self.dfs(root.right, path, res, targetSum)
            path.pop()
        