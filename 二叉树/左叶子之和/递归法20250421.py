# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 左叶子的条件：root.left非空&root.left.left是空&root.left.right是空
# 时间复杂度：O(n)
# 使用递归的方式遍历二叉树的所有节点，并且每个节点都会进行一次叶子节点的判断
# 空间复杂度：O(n)（最坏情况下为链表），平均情况为O(logn)（平衡二叉树）
# 递归调用栈的深度取决于二叉树的高度，最坏情况下二叉树会退化为链表，此时树的高度为n

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        leftValue=0
        if root.left is not None and root.left.left is None and root.left.right is None:
            leftValue=root.left.val
        return leftValue+self.sumOfLeftLeaves(root.left)+self.sumOfLeftLeaves(root.right)
        