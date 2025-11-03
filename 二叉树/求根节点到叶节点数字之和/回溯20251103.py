# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = []
        self.traversal(root, [], res)
        return sum(res)
    
    def traversal(self, root, path, res):
        if root is None:
            return None
        path.append(root.val)
        if root.left is None and root.right is None:
            res.append(self.get_sum(path[:]))
        if root.left:
            self.traversal(root.left, path, res)
            path.pop()
        if root.right:
            self.traversal(root.right, path, res)
            path.pop()
    
    def get_sum(self, path):
        length = len(path)
        ans = 0
        for i in range(len(path)):
            ans = ans*10+path[i]
        return ans
    