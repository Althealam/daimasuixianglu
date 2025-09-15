# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = self.inorder(root)
        for i in range(1, len(res)):
            if res[i]-res[i-1]<=0:
                return False
        return True
    
    def inorder(self, root):
        if not root:
            return []
        res = []
        def dfs(node):
            if node.left:
                dfs(node.left)
            res.append(node.val)
            if node.right:
                dfs(node.right)
            return res
        dfs(root)
        return res
        