# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
      res = []
      path = []
      self.dfs(root, targetSum, path, res)
      if len(res)!=0:
        return True
      return False
    
    def dfs(self, node, targetSum, path, res):
      if not node:
        return None
      path.append(node.val)
      if node.left is None and node.right is None and sum(path[:])==targetSum:
        res.append(path[:])
        return 
      if node.left:
        self.dfs(node.left, targetSum, path, res)
        path.pop()
      if node.right:
        self.dfs(node.right, targetSum, path, res)
        path.pop()
        