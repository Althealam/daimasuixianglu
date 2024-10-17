# 方法：递归法
# 时间复杂度：O(n)
# 空间复杂度：最坏情况下为O(n)，最好情况下为O(logn)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.getNodesNum(root)
    
    def getNodesNum(self,cur):
        if not cur:
            return 0
        leftNum=self.getNodesNum(cur.left) # 左
        rightNum=self.getNodesNum(cur.right) # 右
        treeNum=leftNum+rightNum+1 # 中
        return treeNum