# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        res = []
        self.dfs(root, res, [])
        return res
    
    def dfs(self, root, res, path):
        if root is None:
            return None
        path.append(str(root.val))
        if root.left is None and root.right is None: # the stop criterion
            res.append('->'.join(path[:]))
        if root.left:
            self.dfs(root.left, res, path)
            path.pop()
        if root.right:
            self.dfs(root.right, res, path)
            path.pop()
