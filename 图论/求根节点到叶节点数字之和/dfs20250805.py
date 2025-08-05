# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 时间复杂度：O(n)，每个节点访问一次
# 空间复杂度：O(n) 空间复杂度取决于递归调用栈的空间，递归栈的深度等于二叉树的高度，最坏情况下二叉树的高度为节点的个数
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, prevTotal):
            if not node:
                return 0
            total = prevTotal*10+node.val
            if not node.left and not node.right:
                return total
            else:
                return dfs(node.left, total)+dfs(node.right, total)
        return dfs(root, 0)
        
            
        