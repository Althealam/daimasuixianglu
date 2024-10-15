# 方法：迭代法（后序遍历）
# 时间复杂度：O(n)
# 1. 节点访问：在迭代过程中，每个节点都被访问一次
# 2. 操作：对于每个节点，算法执行一次交换左右子节点的操作
# 空间复杂度：O(h)
# 1. 栈存储：在迭代过程中，使用一个栈来存储待访问的节点。在最坏的情况下，也就是二叉树完全不平衡，每个节点都只有右节点，栈的最大大小将达到二叉树的高度h
# 2. 总结：对于一个完全平衡的二叉树，高度h是log(n)，栈的最大大小是log(n)；对于一个完全不平衡的二叉树，高度h可以接近n，栈的最大大小是n。
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
        stack=[root]
        while stack:
            node=stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            node.left, node.right=node.right, node.left
        return root