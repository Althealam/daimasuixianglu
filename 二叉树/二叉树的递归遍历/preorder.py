class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preordertraversal(self, root):
        res = []

        def dfs(node):
            if node is None:
                return
            
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return res

root = TreeNode(val=0)
root.left = TreeNode(val=1)
root.right = TreeNode(val=2)
solution = Solution()
res = solution.preordertraversal(root)
print(res)