class Solution:
    def preorderTraversal(self, root):
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