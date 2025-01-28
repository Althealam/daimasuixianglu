# 方法：递归法
# 时间复杂度：O(n)
# 空间复杂度：O(logn)，平均是O(logn)，最坏情况下是O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        return self.getNodeNum(root)

    def getNodeNum(self, cur):
        # 如果是空节点，则返回0
        if not cur:
            return 0
        # 计算左边节点的数目
        leftNum=self.getNodeNum(cur.left)
        # 计算右边节点的数目
        rightNum=self.getNodeNum(cur.right)
        # 记录整棵树的数目，包含当前节点
        treeNum=leftNum+rightNum+1
        return treeNum
        