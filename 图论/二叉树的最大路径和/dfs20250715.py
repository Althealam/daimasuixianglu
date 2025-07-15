# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 本质：在以该节点为根节点的子树中寻找以该节点为起点的一条路径，使得该路径上的节点值之和最大
# 思路：
# 空节点的最大贡献值为0
# 非空节点的最大贡献值等于节点值与其子节点的最大贡献值之和

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf') # 最大路径和

        def dfs(node):
            if node is None:
                return 0
            
            # 递归计算左右子节点的最大贡献值
            # 只有在最大贡献值大于0的时候才会选取对应的子节点
            l_val = max(dfs(node.left), 0)
            r_val = max(dfs(node.right), 0)

            # 节点的最大路径和取决于该节点的值和该节点的左右子节点的最大贡献值
            val = node.val+l_val+r_val

            # 更新答案
            nonlocal ans 
            ans = max(ans, val)

            # 返回节点的最大贡献值
            return max(l_val, r_val)+node.val
        dfs(root)
        return ans