# 思路：判断左右子树是否是翻转的，只能通过后序遍历来实现，因为我们需要通过递归函数的返回值来判断两个子树的内侧节点和外侧节点是否是相等的
# 时间复杂度：O(n)
# 空间复杂度：O(logn)（平均情况下是logn，最坏情况下是n）

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
        return self.compare(root.left,root.right)
    
    def compare(self, left, right):
        # 排除空节点的情况
        if left==None and right!=None:
            return False
        elif left!=None and right==None:
            return False
        elif left==None and right==None: # 注意，如果左右孩子为空，应该是返回True，而不是返回False
            return True
        
        # 排除左右孩子节点的值不相同的情况
        if left.val!=right.val:
            return False
        
        # 左右孩子节点都不为空，并且左右孩子节点的值相同的情况
        outside=self.compare(left.left,right.right) # 外侧的比较
        inside=self.compare(left.right,right.left) # 内侧的比较

        isSame=outside and inside
        return isSame

        