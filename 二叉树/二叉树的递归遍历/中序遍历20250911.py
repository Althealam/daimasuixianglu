class Solution:
    def inorderTraversal(self, root):
        res = []
        self.dfs(root, res)
        return res

    def dfs(self, root, res):
        if not root:
            return None
        self.dfs(root.left, res)
        res.append(root.val)
        self.dfs(root.right, res)
