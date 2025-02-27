# 时间复杂度：O(n)
# 对于每个节点，代码会递归的访问其左子树和右子树，并且这个递归是一个深度优先搜索的过程，每次递归调用会处理一个新的节点，并且每个节点会被访问依次
# 空间复杂度：O(n)
# 空间复杂度主要取决于递归栈的深度。
# 最坏情况下二叉树是一条链，此时h=n。那么就是O(n)
# 最好情况下二叉树是平衡二叉树，此时h=logn。那么就是O(logn)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0
        if root.left is None and root.val is None:
            return root.val
        # 偷父节点，并且不偷父节点的左右孩子节点
        val1=root.val
        # 偷父节点的时候，不可以偷其左孩子节点，但是可以偷其左孩子节点的孩子节点
        if root.left:
            val1+=self.rob(root.left.left)+self.rob(root.left.right)
        # 偷父节点的时候，不可以偷其右孩子节点，但是可以偷其右孩子节点的孩子节点
        if root.right:
            val1+=self.rob(root.right.left)+self.rob(root.right.right)

        # 不偷父节点，改成偷父节点的左右孩子节点
        val2=self.rob(root.left)+self.rob(root.right)
        return max(val1, val2)