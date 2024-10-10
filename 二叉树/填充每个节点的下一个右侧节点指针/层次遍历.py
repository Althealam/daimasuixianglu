# 方法：层次遍历
# 分析：层次遍历基于广度优先搜索，它与广度优先搜索的不同之处在于广度优先搜索每次只会取出一个节点扩展，而层次遍历会每次将队列中的所有元素拿出来扩展，这样能保证每次从队列中拿出来遍历的元素都是属于同一层的，因此我们可以在遍历的过程中修改每个节点的next指针，同时扩展下一层的新队列

# 时间复杂度：O(n)，每个节点会被访问一次并且只会被访问一次，即从队列中弹出
# 空间复杂度：O(n)。广度优先遍历的复杂度取决于一个层级上的最大元素数量
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

import collections

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        
        # 初始化队列，同时将第一层节点加入队列中，即根节点
        Q=collections.deque([root])

        # 外层的while循环迭代的是层数
        while Q:
            # 记录当前队列大小
            size=len(Q)

            # 遍历这一层的所有节点
            for i in range(size):
                # 从队首取出元素
                node=Q.popleft()

                # 连接
                if i<size-1:
                    node.next=Q[0]
                
                # 扩展下一层节点
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
        
        # 返回根节点
        return root
        