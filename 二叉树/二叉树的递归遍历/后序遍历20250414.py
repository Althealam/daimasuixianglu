# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        res=self.dfs(res, root)
        return res

    
    def dfs(self, res, node):
        if node is None:
            return []
        self.dfs(res, node.left)
        self.dfs(res, node.right)
        res.append(node.val)
        return res
        