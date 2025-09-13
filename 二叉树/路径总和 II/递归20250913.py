# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        path = []
        self.dfs(root, targetSum, path, result)
        return result
    
    def dfs(self, root, targetSum, path, result):
        if not root:
            return None
        path.append(root.val)
        if root.left is None and root.right is None and sum(path[:])==targetSum:
            result.append(path[:])
            return 
        if root.left:
            self.dfs(root.left, targetSum, path, result)
            path.pop()
        if root.right:
            self.dfs(root.right, targetSum, path, result)
            path.pop()