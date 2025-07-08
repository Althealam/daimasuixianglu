# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 时间复杂度：O(n)
# 空间复杂度：O(n)
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.ans = [] # 计算每条由根节点到叶子节点的路径和

        def dfs(node, cnt):
            if node is None:
                return 
            cnt+=node.val
            if node.left is None and node.right is None:
                self.ans.append(cnt)
                cnt-=node.val
                return 
            dfs(node.left, cnt)
            dfs(node.right, cnt)
        
        dfs(root, 0)
        return targetSum in self.ans
