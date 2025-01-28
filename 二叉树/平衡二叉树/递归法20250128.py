# 思路：计算左右子树的高度，并且比较高度差是否大于1，如果大于1的话就不是平衡二叉树
# 方法：递归法
# 时间复杂度：O(n)
# 空间复杂度：平均空间复杂度是O(logn)，最坏情况下空间复杂度是O(n)
# 空间复杂度取决于递归调用栈的深度

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.getheight(root)!=-1


    def getheight(self,node):
        """
        用递归的方法计算树的高度
        1. 递归计算左子树高度，如果左子树不平衡则返回-1
        2. 递归计算右子树高度，如果右子树不平衡则返回-1
        3. 检查左右子树高度差，如果超过1，返回-1表示不平衡
        4. 如果左右子树平衡并且高度差不超过1，返回当前子树的高度（左右子树高度的较大值+1）
        """
        if not node:
            return 0
        left_height=self.getheight(node.left)
        if left_height==-1:
            return -1
        right_height=self.getheight(node.right)
        if right_height==-1:
            return -1
        if abs(left_height-right_height)>1:
            return -1
        return max(left_height,right_height)+1
    