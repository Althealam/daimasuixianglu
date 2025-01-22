# 思路：相当于上一题二叉树的层序遍历，最后反转数组即可
# 时间复杂度：O(n)
# 1. 外层while queue会持续运行直到队列为空
# 2. 内层的循环次数等于当前层的节点数量
# 3. 反转操作的时间复杂度是O(n)，相当于复制整个列表
# 空间复杂度：O(n)
# 1. queue最坏情况下存储的节点数最多为最宽层的节点数
# 对于满二叉树，最宽层的节点数为n/2
# 2. result存储所有节点的值，因此最终存储的元素数量也是n个节点的值

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []

        result=[]
        queue=collections.deque([root]) # 构建队列
        while queue:
            level=[] # 存储这层的节点值 
            for _ in range(len(queue)): # 遍历队列里的值
                node=queue.popleft() # 弹出左边的节点
                level.append(node.val) # 将左边的节点加入到该层的数组
                # 放入节点的左右节点
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result[::-1]



        