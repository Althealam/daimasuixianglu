# 方法：递归+回溯（精简版）

# 时间复杂度：O(n)
# 1. 树的遍历：递归函数 traversal 会遍历整棵树。对于每个非叶子节点，函数会递归遍历其左子树和右子树。
# 2. 单个结点的处理：在每次递归调用中，对每个节点只进行了常数次操作，例如减法和加法操作
# 空间复杂度：最坏情况下为O(n)，最好情况下为O(logn)
# 1. 递归栈空间：由于使用了递归，栈的深度取决于树的高度。对于一棵平衡二叉树，树的高度为 O(log N)；对于最坏情况下的退化树（链式结构），树的高度为 O(N)。
# 2. 额外空间：除了递归栈之外，该算法没有使用额外的空间（例如数组或哈希表）。递归过程中每次只在函数栈中存储局部变量 cur 和 count。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):        
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right and targetSum == root.val:
            return True
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
  