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
        self.dfs(res, [], root)
        return res
    
    def dfs(self, res, path, node):
        if not node:
            return None
        path.append(node.val)
        if node.left is None and node.right is None:
            res.append("->".join(map(str, path[:])))
            return 
        if node.left:
            self.dfs(res, path, node.left)
            path.pop()
        if node.right:
            self.dfs(res, path, node.right)
            path.pop()

        