# 方法：递归法
# 思路：将插入节点的值与根节点比较即可，然后插入到叶子结点下面即可，这是最简单的方法
# 时间复杂度：取决于树的高度
# 1. 平衡树：O(logn)
# 2. 不平衡树：O(n)
# 空间复杂度：取决于递归调用栈的深度
# 在递归过程中，每次调用都会在调用栈上添加一个新的栈
# 1. 平衡树：O(logn)
# 2. 不平衡树：O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if root==None: # 达到叶子结点，并且这是我们需要插入的位置
            node=TreeNode(val) # 定义我们需要插入的叶子结点
            return node
        if val<root.val:
            root.left=self.insertIntoBST(root.left,val) # 将叶子结点与其根节点连接起来，利用赋值来实现
        if val>root.val:
            root.right=self.insertIntoBST(root.right,val)
        return root
        