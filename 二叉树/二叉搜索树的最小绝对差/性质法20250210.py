# 思路：用中序遍历保存二叉搜索树的数组，计算两两元素之间的差，找到最小值
# 时间复杂度：O(n)
# 1. 中序遍历：访问二叉树的每个节点 O(n)
# 2. 计算最小差值：遍历vector来找出相邻元素之间的最小差值 O(n)
# 空间复杂度：O(n)
# 1. 递归调用栈：中序遍历是用递归实现的，递归调用栈的深度取决于二叉树的高度，因此为O(h)
# 2. 存储中序遍历的结果列表：self.vector为O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    # 利用中序遍历获取二叉搜索树的有序数组
    def __init__(self):
        self.vector=[]
    
    def traversal(self,root):
        if root is None:
            return 
        self.traversal(root.left)
        self.vector.append(root.val)
        self.traversal(root.right)

    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.vector=[]
        self.traversal(root)
        result=float('inf')
        # 找到有序数组的最小值
        for i in range(1,len(self.vector)):
            result=min(result, self.vector[i]-self.vector[i-1])
        return result
    

        