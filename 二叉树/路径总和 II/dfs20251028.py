# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        self.dfs(res, [], targetSum, root)
        return res
    
    def dfs(self, res, path, targetSum, root):
        if not root:
            return None
        path.append(root.val)
        if root.left is None and root.right is None and sum(path)==targetSum:
            res.append(path[:])
        if root.left:
            self.dfs(res, path, targetSum, root.left)
            path.pop()
        if root.right:
            self.dfs(res, path, targetSum, root.right)
            path.pop()