# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        res = self.dfs(root, res)
        return res
    
    def dfs(self, node, res):
        if node is None:
            return []
        res.append(node.val)
        self.dfs(node.left, res)
        self.dfs(node.right, res)
        return res
