# 方法：递归法（精简版）
# 时间复杂度：O(n)
# 空间复杂度：最坏情况下为O(n)，最好情况下为O(logn)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return 1+self.countNodes(root.left)+self.countNodes(root.right)
        