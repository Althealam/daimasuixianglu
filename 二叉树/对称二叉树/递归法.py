# 方法：递归法
# 思路：判断根节点的左右孩子节点是否是翻转二叉树，如果是的话，这棵树就是一个对称二叉树
# 同是外侧的节点进行比较，同是内侧的节点进行比较
# 这道题只能使用后序遍历，因为我们要通过递归函数的返回值来判断两个子树的内侧节点和外侧节点是否相等
# 一棵树的遍历顺序是左右中，另外一棵树的遍历顺序是右左中

# 分析：
# 递归三部曲
# 1. 确定递归函数的参数和返回值：参数是两个树，也就是左子树节点和右子树节点
# 2. 确定终止条件
# （1）左为空，右不为空/左不为空，右为空：return false
# （2）左右都为空：return true
# （3）左右都不为空：比较节点值
# 3. 确定单层递归逻辑
# （1）比较二叉树外侧是否对称
# （2）比较二叉树内侧是否对称

# 时间复杂度：O(n)，每个节点都被访问一次
# 空间复杂度：O(h)，递归的空间复杂度取决于递归的深度，也就是调用栈的大小

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return true
        return self.compare(root.left,root.right)
    
    def compare(self,left,right):
        # 首先排除空节点的情况
        if left==None and right!=None: return False
        elif left!=None and right==None: return False
        elif left==None and right==None: return True
        elif left.val!=right.val: return False

        # 左右节点都不为空，并且数值相等
        outside=self.compare(left.left,right.right) # 左
        inside=self.compare(left.right,right.left) # 右
        isSame=outside and inside # 中
        return isSame
        