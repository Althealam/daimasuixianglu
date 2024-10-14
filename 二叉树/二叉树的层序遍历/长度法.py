# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue=collections.deque([root])
        result=[] # 用于存储每层节点值的列表
        while queue:
            level=[] # 存储当前层的节点
            for _ in range(len(queue)):
                cur=queue.popleft() # 从队列中取出元素
                level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            result.append(level)
        return result        