# 方法：递归法（稍微复杂一点的版本）
# 时间复杂度：O(n)，每个节点都会被访问一次
# 空间复杂度
# 最坏情况下是O(n)，二叉树是单链状（即所有节点只有左子树/右子树），递归的深度会达到n
# 最佳情况下是O(logn)，二叉树是平衡的，比如完全二叉树，那么递归的最大深度是树的高度h=logn

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.getdepth(root)
    
    def getdepth(self,node):
        if not node:
            return 0
        leftheight=self.getdepth(node.left)
        rightheight=self.getdepth(node.right)
        height=1+max(leftheight,rightheight)
        return height

        