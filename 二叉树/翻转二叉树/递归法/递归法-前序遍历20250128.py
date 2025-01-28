# 方法：递归法（前序遍历）
# 思路：遇到每个节点，只要该节点的孩子节点不为空，则反转其孩子节点，只用前序遍历后者后序遍历
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 时间复杂度：O(n），每个节点都只访问一次，并且在访问每个节点的时候进行的操作都是常数级别的
# 空间复杂度：O(logn），平均情况下对于平衡二叉树，递归调用栈的深度是O(logn)，最坏情况下退化为链表，深度为n

class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None
        root.left, root.right=root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root