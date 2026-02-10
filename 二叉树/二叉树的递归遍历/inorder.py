class Solution:
    def inordertraversal(self, root):
        res = []

        def dfs(node):
            if node is None:
                return 
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        dfs(root)
        return res