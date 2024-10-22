# 方法：递归精简版
# 左叶子定义：左右孩子为空时，是叶子结点；
# 思路：遍历到父结点的时候，判断左孩子是否为空，不为空的话，判断左孩子的左右节点是否为空
# 1. 确定递归函数的参数和返回值：传入树的根节点，递归函数的返回值为数值之和
# 2. 确定终止条件：
# （1）遍历到空节点，左叶子值一定为0，返回0
# （2）遍历到叶子结点，返回0（因为需要遍历到父结点，才能判断子结点是不是左叶子）
# 3. 确定单层递归的逻辑：遇到左叶子结点的时候，记录数值，然后通过递归求左子树左叶子结点之和，右子树左叶子结点之和，相加便是整个树的左叶子之和
# 分析：使用后序遍历，这样可以收集左节点的情况后返回给根节点
# 时间复杂度：O(n)，每个节点会被访问一次
# 空间复杂度：最坏情况下为O(n)（树呈现链状，退化成一条线，递归的深度等于树的高度）；平衡二叉树时，树的高度为logn，此时为O(logn)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0
        leftValue=0
        if root.left is not None and root.left.left is None and root.left.right is None:
            leftValue=root.left.val
        return leftValue+self.sumOfLeftLeaves(root.left)+self.sumOfLeftLeaves(root.right)