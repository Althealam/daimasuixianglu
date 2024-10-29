# 方法：递归法-前序遍历-修改root1
# 1. 确定递归函数的参数和返回值：传入两个二叉树的根节点，返回值就是合并之后二叉树的根节点
# 2. 确定终止条件：t1==NULL时为t2；t2==NULL时为t1
# 3. 确定单层递归的逻辑：将两棵树的元素加到一起
# 合并规则：如果有相同的节点，就将两个节点合并相加
# 思路：利用前序遍历来处理两棵树（中序和后序也可以，只是前序比较直观）

# 时间复杂度：O(n)
# 代码使用递归方法遍历两棵二叉树，对于每个节点，都会进行一次递归调用

# 空间复杂度：空间复杂度由递归调用栈的深度决定
# （1）树为平衡二叉树时，空间复杂度为O(logn)
# （2）树为链状的，空间复杂度为O(n)
# 代码在合并两棵树时，每次递归调用都处理一对对应节点，这意味着每次递归都会深入到树的一层。


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root1:
            return root2
        if not root2:
            return root1
        root1.val+=root2.val
        root1.left=self.mergeTrees(root1.left,root2.left)
        root1.right=self.mergeTrees(root1.right,root2.right)

        return root1 # 重复使用题目给的节点，而不是创建新节点
        