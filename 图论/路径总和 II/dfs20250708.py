# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.ans = []
        def dfs(node, path):
            if not root:
                return None
            path.append(node.val)
            if node.left is None and node.right is None and sum(path)==targetSum:
                self.ans.append(path[:])
                return 
            if node.left:
                dfs(node.left, path)
                path.pop()
            if node.right:
                dfs(node.right, path)
                path.pop()
        dfs(root, [])
        return self.ans

        