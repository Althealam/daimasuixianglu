# 思路：由图可以看出遍历的顺序是右中左
# 递归法，先递归右子树，再在中节点进行累加的操作，最后遍历左子树

# 时间复杂度：O(n)
# 递归函数convertBST会对树中的每个节点都进行一次访问，并且每次访问函数执行的操作都是常数时间
# 空间复杂度：O(h)
# 空间复杂度取决于递归调用栈的深度，并且递归调用栈的深度与二叉树的高度h相关
# 1. 最坏情况：退化为链表 O(n)
# 2. 最好情况：平衡二叉树 O(logn)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.count=0

    def convertBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # 进行递归前，需要判断root是否为空值
        if not root:
            return None

        # 遍历右子树
        self.convertBST(root.right)

        # 中节点
        self.count+=root.val
        root.val=self.count

        # 遍历左子树
        self.convertBST(root.left)

        return root
        