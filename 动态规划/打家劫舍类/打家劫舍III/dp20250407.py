# 本题一定是通过后序遍历来判断是否偷（左右中，由此可以确定是否是同一个父节点）
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dp=self.traversal(root)
        return max(dp)
    
    def traversal(self, node):
        """
        dp数组以及下标的含义：
        dp[0]表示不偷该节点得到的最大金钱
        dp[1]表示偷该节点得到的最大金钱
        :return (val_0, val_1)：分别表示偷和不偷该节点时的最大金额
        """
        # 遇到了叶子节点
        if not node:
            return (0,0)

        left=self.traversal(node.left) # 左
        right=self.traversal(node.right) # 右

        # 中
        # 1. 不偷当前节点，偷子节点
        # (1) left[0]和right[0]表示不偷当前节点的最大金额
        # (2) left[1]和right[1]表示偷当前节点的最大金额
        val_0=max(left[0], left[1])+max(right[0], right[1])
        # 2. 偷当前节点，不偷子节点
        val_1=node.val+left[0]+right[0]

        return (val_0, val_1)
        