# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        path = []
        result = []
        self.traversal(result, path, root)
        return result
    
    def traversal(self, result, path, root):
        path.append(root.val)
        if root.left is None and root.right is None:
            result.append('->'.join(map(str, path)))
            return 
        if root.left:
            self.traversal(result, path, root.left)
            path.pop()
        if root.right:
            self.traversal(result, path, root.right)
            path.pop()

        
        