class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def inorderTraversal(self, root):
        res=[]
        def dfs(node):
            if node is None:
                return 

            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        dfs(root)
        return res
    

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

s = Solution()
print(s.inorderTraversal(root))