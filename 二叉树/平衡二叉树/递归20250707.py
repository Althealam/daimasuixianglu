# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 思路：判断二叉树是否是平衡的
# 子问题：求解二叉树的高度，如果高度差超过1，那么返回-1

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.get_height(root)!=-1
    
    def get_height(self, root):
        if not root:
            return 0
        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)
        if left_height==-1 or right_height==-1 or abs(left_height-right_height)>1:
            return -1
        return max(self.get_height(root.left), self.get_height(root.right))+1