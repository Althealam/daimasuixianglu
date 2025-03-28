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
        while queue:
            size=len(queue)
            level=[]
            for i in range(len(queue)):
                node=queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level[-1])
            # print(level)
            # print(level[-1])
        return result

# 注意：
# 1. array[-1]表示访问array的最后一个元素
# 2. array[:-1]表示从列表的开始到倒数第二个元素
# 3. array[::-1]表示从列表的最后一个元素开始，以步长为-1选取元素

        