# 方法：迭代法（使用队列）

# 时间复杂度：O(n)，使用广度优先搜索来判断二叉树是否对称，遍历整个二叉树的每一个节点，每个节点都要被处理一次
# 空间复杂度：O(n)，空间复杂度由queue决定，在广度优先搜索中，队列中存储的是当前层和下一层的节点

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return true
        queue=collections.deque()
        queue.append(root.left)
        queue.append(root.right)
        while queue: # 判断两个树是否相互翻转
            leftNode=queue.popleft()
            rightNode=queue.popleft()
            if not leftNode and not rightNode: # 左节点为空，右节点为空，则是对称的
                continue 
            
            # 左右一个节点不为空，或者都不为空但是数值不同
            if not leftNode or not rightNode or leftNode.val!=rightNode.val:
                return False
            queue.append(leftNode.left)
            queue.append(rightNode.right)
            queue.append(leftNode.right)
            queue.append(rightNode.left)
        return True