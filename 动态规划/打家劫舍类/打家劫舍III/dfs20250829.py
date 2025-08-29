# 后序遍历：求出每个节点选或者不选的状态下的最大金额
# 1. 选或者不选：如果选择当前节点，那么该节点的左右儿子都不能选；如果不选当前节点，那么可以选择该节点的父亲节点和左右儿子节点
# 2. 递推公式
# （1）选= 左不选+右不选+当前节点值
# （2）不选=max（左选，左不选）+max（右选，右不选）

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        rob, not_rob = self.dfs(root)
        return max(rob, not_rob)
    
    def dfs(self, node):
        if not node:
            return (0, 0)
        left_rob, left_not_rob = self.dfs(node.left)
        right_rob, right_not_rob = self.dfs(node.right)
        not_rob = max(left_rob, left_not_rob)+max(right_rob, right_not_rob)
        rob = node.val+left_not_rob+right_not_rob
        return (rob, not_rob)
        