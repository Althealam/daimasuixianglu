# 方法：层序遍历
# 思路：层序遍历的层数就是二叉树的深度
# 时间复杂度：O(n)，其中n是二叉树的节点个数
# 因为每个节点恰好都被访问一次。在遍历过程中，每个节点都被从队列中取出一次，并将其子节点加入队列。
# 空间复杂度：O(n)
# 在最坏情况下（树完全不平衡，每个节点最多有两个子节点），队列就需要存储所有节点
# 在层序遍历中，队列中存储的节点数最多等于树的最大宽度

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        depth=0 # 树的深度，初始为0
        queue=collections.deque([root]) # 队列，存储当前层的节点

        while queue:
            depth+=1
            for _ in range(len(queue)):
                node=queue.popleft() # 当前处理的节点
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth
        