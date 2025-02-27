# 1. dp数组以及下标的含义：
# （1）dp[0]表示不选择当前节点时，在以当前节点为根的子树中能获得的最大收益
# （2）dp[1]表示选择当前节点时，在以当前节点为根的子树中能获得的最大收益
# 2. 递推公式
# （1）不选择当前节点：val_0=max(left[0], left[1])+max(right[0], right[1])
# （2）选择当前节点：val_1=node.val+left[0]+right[0]
# 3. 遍历顺序：后序遍历（左右中），因为需要得到左右子树的结果后才能计算中节点的结果
# 4. 初始化：遇到空节点的时候是递归的终止条件

# 时间复杂度：O(n)
# 1. 后序遍历二叉树的每个节点，每个节点都进行常数次操作
# 2. 每个节点都会被访问并且仅访问一次。在每个节点处，计算val_0和val_1以及返回结果的操作时间的复杂度都为O(1)

# 空间复杂度：O(n)
# 由递归调用栈的深度决定
# 最坏情况下二叉树是一条链，此时h=n，那么为O(n)
# 最好情况下二叉树是平衡的，此时h=logn，那么O(logn)

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
        dp=self.traversal(root)
        return max(dp)
    
    def traversal(self, node):
        # 递归终止条件，遇到了空节点，此时不偷
        if not node:
            return (0,0)
        left=self.traversal(node.left)
        right=self.traversal(node.right)
        # 不偷当前节点，偷子节点
        val_0=max(left[0], left[1])+max(right[0], right[1])
        # 偷当前节点，不偷子节点
        val_1=node.val+left[0]+right[0]

        return (val_0, val_1)