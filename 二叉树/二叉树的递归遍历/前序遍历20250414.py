# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[] # 前序遍历的结果
        res=self.dfs(res, root)
        return res 

    def dfs(self, res, node):
        if node is None:
            return []
        res.append(node.val)
        self.dfs(res, node.left)
        self.dfs(res, node.right)

        return res
        