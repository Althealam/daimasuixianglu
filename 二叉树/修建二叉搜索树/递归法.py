# 方法：递归法
# 分析：
# 1. 如果要删除的节点小于low，那么其左子树也需要删除，但是其右子树可能是需要保留的
# 2. 如果要删除的节点大于high，那么其右子树也需要删除，但是其左子树可能是需要保留的

# 时间复杂度：O(n)
# 在修剪过程中，每个节点会被访问一次，并且做出是否保留、修剪左子树、或修剪右子树的判断

# 空间复杂度：平均情况下为O(logn)，最坏情况下为O(n)
# 代码使用递归实现树的修剪，因此空间复杂度取决于递归栈得到深度，递归的深度等于树的高度

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def trimBST(self,root,low,high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: Optional[TreeNode]
        """
        if root==None:
            return None
        if root.val<low: # 不能直接return right，因为并不是所有的右子树的节点都一定符合要求
            right=self.trimBST(root.right,low,high)
            return right
        if root.val>high:
            left=self.trimBST(root.left,low,high)
            return left
        root.left=self.trimBST(root.left,low,high) # 修建左子树
        root.right=self.trimBST(root.right,low,high) # 修改右子树
        return root

        
        