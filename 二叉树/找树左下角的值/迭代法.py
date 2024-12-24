# 方法：迭代法
# 思路：使用层序遍历，记录最后一行第一个节点的数值即可
# 时间复杂度：使用广度优先搜索（BFS）遍历树中的每个节点，并且每个节点只会被出队和入队一次，时间复杂度为O(n)
# 空间复杂度：最好的情况下为O(1)，最坏的情况下为O(n)
# 空间复杂度由队列的最大长度决定，最坏情况下，队列的大小等于当前层节点的数量，树最宽的层会决定队列的最大长度。
# （1）在最坏的情况下，如果树是完全平衡的二叉树，队列的最大长度会发生在树的最后一层，此时最后一层最多会有 n/2 个节点。因此，空间复杂度为 O(n)。
# （2）如果树是非常不平衡的（例如退化为链表），则队列中最多只有一个节点，空间复杂度为 O(1)。
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0
        queue=deque()
        queue.append(root)
        result=0
        while queue:
            size=len(queue)
            for i in range(size):
                node=queue.popleft() # 找到这一层的第一个值
                if i==0:
                    result=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result