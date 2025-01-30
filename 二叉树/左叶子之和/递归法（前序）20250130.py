# 方法：递归法（前序遍历）
# 思路：遍历每个节点，判断是否是左叶子
# 左叶子的定义：节点A的左孩子不为空，并且该左孩子的左右孩子都为空，可以判断节点A的左孩子为左叶子

# 时间复杂度：O(n) 每个节点都会被访问并且仅仅访问一次
# 空间复杂度：O(n)
# 递归调用会使用系统栈来存储每一层的调用信息。
# 1. 最坏情况：二叉树退化为链表，递归的深度达到n，此时的空间复杂度为O(n)
# 2. 平均情况：二叉树是平衡的，递归深度为logn，此时的空间复杂度为O(logn)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0
        sum_value=0 # 计算左叶子节点和
        if root.left is not None and root.left.left is None and root.left.right is None:
            sum_value=root.left.val
        return sum_value+self.sumOfLeftLeaves(root.left)+self.sumOfLeftLeaves(root.right)