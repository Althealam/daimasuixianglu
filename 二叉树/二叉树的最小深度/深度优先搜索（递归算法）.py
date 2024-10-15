# 方法：深度优先搜索（递归算法）
# 思路：使用深度优先搜索的方法，遍历整棵树，记录最小深度
# 对于每一个非叶子结点，我们只需要分别计算其左右子树的最小叶子结点深度
# 时间复杂度：O(n)，每个节点访问一次，因此算法会执行n次调用
# 空间复杂度：O(h)，取决于递归调用的深度
# 1. 最坏情况下：二叉树完全不平衡，比如形成一个链状结构，递归深度将会和二叉树的高度相同，同时也和二叉树的节点个数相同，也就是O(n)
# 2. 平均情况下：如果二叉树是平衡的。那么高度将是log(n)，因此递归深度是log(n)。在这种情况下，递归栈中的元素数量将会是log(n)，因此空间复杂度是O(log n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        # 如果root没有左右子节点，即root是一个叶子结点，则返回1
        if not root.left and not root.right:
            return 1
        
        min_depth=10**9
        # 递归调用self.minDepth()，计算左子节点的最小深度，并且和min_depth进行比较
        if root.left:
            min_depth=min(self.minDepth(root.left),min_depth)
        # 递归调用self.minDepth()，计算右子节点的最小深度，并且和min_depth进行比较
        if root.right:
            min_depth=min(self.minDepth(root.right),min_depth)
        
        # +1是因为要包含当前节点本身
        return min_depth+1