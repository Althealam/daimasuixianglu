class Solution:
    def preorderTraversal(self, root):
        res = []
        self.dfs(root, res)
        return res
    def dfs(self, root, res):
        if root is None:
            return 
        self.dfs(root.left)
        res.append(root.val)
        self.dfs(root.right)
        return res
