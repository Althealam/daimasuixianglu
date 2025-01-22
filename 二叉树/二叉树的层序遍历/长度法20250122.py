# 思路：定义队列，然后每次遍历孩子节点的时候就把孩子节点放到队列中，最后弹出队列中的元素即可
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 时间复杂度：O(n)
# 空间复杂度：O(n) 由queue和result决定，queue在最坏情况下会存储二叉树最宽一层的节点，result存储了每个层的节点值

from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result=[]
        queue=collections.deque([root]) # 用来存元素的队列
        while queue: 
            level=[] # 该层的元素值
            for _ in range(len(queue)):
                cur=queue.popleft()
                level.append(cur.val)
                # 开始放入孩子节点，注意不是放入孩子节点的值，而是放入节点
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            result.append(level) 
        return result       