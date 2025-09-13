# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        # 前序遍历
        h = abs(self.get_height(root.left)-self.get_height(root.right))<=1
        if h==True:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False
    
    def get_height(self, root):
        """给定节点 求出高度"""
        if root is None:
            return 0
        return max(self.get_height(root.left), self.get_height(root.right))+1
        