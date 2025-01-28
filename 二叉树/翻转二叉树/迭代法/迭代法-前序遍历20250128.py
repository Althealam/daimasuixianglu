# 方法：迭代法
# 思路：用栈来模拟递归法，类比一下层序遍历，注意栈是先进后出的，因此对于前序遍历，需要先进入右节点，再进入左节点，才是中左右的顺序
# 时间复杂度：O(n）
# 空间负载的：平均空间复杂度是O(logn)，最坏情况下空间复杂度是O(n)
# 对于平衡二叉树，栈的最大深度近似为树的高度h，而平衡二叉树的高度h=logn
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None
        stack=[root]
        while stack:
            node=stack.pop()
            node.left, node.right=node.right, node.left
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return root