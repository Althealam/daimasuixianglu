# 方法：递归法
# 平衡二叉树的定义：在二叉树的所有子树中，左右节点的高度差不超过1
# 高度：到叶子结点的距离（求高度用后序遍历，后序遍历是向上遍历）
# 深度：到根节点的距离（求深度用前序遍历，前序遍历是向下遍历）
# 分析：本题使用后序遍历，才能得到左子树和右子树的高度差
# 时间复杂度：O(n)，每个节点都会被访问一次
# 空间复杂度：O(logn)（平衡树）或者O(n)（不平衡树）
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
        return self.get_hight(root)!=-1
    def get_hight(self,node):
        if not node:
            return 0
        left=self.get_hight(node.left)
        right=self.get_hight(node.right)
        if left==-1 or right==-1 or abs(left-right)>1:
            return -1
        return max(left,right)+1
        