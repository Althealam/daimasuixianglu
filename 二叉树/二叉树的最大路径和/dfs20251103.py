# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf')

        def dfs(node):
            if node is None:
                return 0
            # left node（左子树的贡献值）
            l_val = max(dfs(node.left), 0)
            # right node（右子树的贡献值）
            r_val = max(dfs(node.right), 0)
            nonlocal ans
            # 答案值
            val = node.val+l_val+r_val
            ans = max(ans, val)
            return max(l_val, r_val)+node.val # 中节点的贡献值（当前一个分支的最大值）
        dfs(root)
        return ans