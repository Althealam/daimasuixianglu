# 方法：迭代法（层序遍历的思路）
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 时间复杂度：O(n)
# 空间复杂度：O(n)，取决于queue的大小，最坏情况下，对于完全二叉树，最底层的节点数最多，其数量接近n/2，因此队列中最多会存储n/2个节点
from collections import deque
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        queue=collections.deque()
        result=0 # 用来记录节点数
        if root:
            queue.append(root)
        # 层序遍历
        while queue:
            size=len(queue)
            for i in range(size):
                # 只要有节点可以弹出来，就直接把结果数加1
                node=queue.popleft()
                result+=1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result