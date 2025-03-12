# 思路：层序遍历，然后找到每一层的最后一个元素

# 时间复杂度：O(n)
# 空间复杂度：O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
import collections
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        result=[]
        queue=collections.deque([root]) 
        # 如果使用queue=collections.deque([root]) 需要使用queue.popleft()
        # 如果使用queue=[root] 需要使用queue.pop(0) 表示弹出第一个元素，这个是队列
        while queue:
            size=len(queue)
            for i in range(size):
                node=queue.popleft()
                if i==size-1: # 注意这里一定要用size来替代，因为queue.popleft()后长度会发生变化
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result


        