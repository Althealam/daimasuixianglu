# 方法：广度优先搜索
# 思路：有关层序遍历的题优先使用广度优先搜索
# 具体思路：首先将根节点root放入队列中，然后在广度优先搜索的每一轮中，我们首先记录下当前队列中包含的节点个数（记为cnt），即表示上一层的节点个数。在这之后，我们从队列中依次取出节点，直到取出了上一层的全部cnt个节点为止。当取出节点cur时，我们将cur的值放入一个临时列表，再将cur的所有子节点全部放入队列中。
# 一轮遍历完成后，临时列表中就存放了当前层所有节点的值
# 时间复杂度：O(n)，其中n是树中包含的节点个数
# 空间复杂度：O(n)，即为队列需要使用的空间。最坏的情况下，树只有两层，并且最后一层有n-1个节点，此时就需要O(n)的空间
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val # 节点的值
        self.children = children # 子节点列表
"""

from collections import deque

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []

        ans=list()
        q=deque([root])

        while q:
            cnt=len(q)
            level=list()
            for _ in range(cnt):
                cur=q.popleft()
                level.append(cur.val)
                for chile in cur.children:
                    q.append(children)
            ans.append(level)
        return ans
