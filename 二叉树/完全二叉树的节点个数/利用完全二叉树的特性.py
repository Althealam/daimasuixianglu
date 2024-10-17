# 方法：利用完全二叉树的特性
# 时间复杂度：O(logn)
# 空间复杂度：O(logn)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def countNodes(self,root):
        if not root:
            return 0
        count=1
        left=root.left
        right=root.right
        while left and right:
            count+=1
            left=left.left
            right=right.right
        if not left and not right: # 同时到底--满二叉树
            return 2**count-1
        return 1+self.countNodes(root.left)+self.countNodes(root.right)
             