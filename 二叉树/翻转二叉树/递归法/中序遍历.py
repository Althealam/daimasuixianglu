# 方法：递归法（中序遍历）
# 递归三部曲：
# 1. 确定递归函数的参数和返回值
# 2. 确定终止条件
# 3. 确定单层递归的逻辑
# 注意：交换的是指针，不是数值
# 中序遍历相对于前序遍历和后序遍历比较复杂
# 思路：将每个节点的左右孩子节点翻转一下，就可以达到整体翻转的效果
# 时间复杂度：O(n)
# 1. 节点访问：递归过程中，每个节点都被访问一次
# 2. 操作：每个节点，算法执行一次交换左右子节点的操作
# 空间复杂度：O(n)
# 1. 递归栈：递归过程中，递归的深度取决于二叉树的高度。最坏情况下，二叉树可能是完全不平衡的，也就是呈现链条状，这时是O(n)
# 2. 递归栈的最大大小是递归深度，因此空间复杂度是O(h)，其中h是二叉树的高度。
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        self.invertTree(root.left)
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        
        return root