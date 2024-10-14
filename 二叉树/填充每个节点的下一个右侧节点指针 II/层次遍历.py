# 层序遍历
# 这道题和“填充每个节点的下一个右侧节点指针”不同的是，这道题不是完全二叉树，父节点不一定有两个子节点
# 但是仍然可以使用同样的方法

# 时间复杂度：O(n)
# 空间复杂度：O(n)

# 例子：
#     1
#    / \
#   2   3
#  / \
# 4   5

# 1. 初始化：Q = deque([1])（根节点）
# 2. 第一层
# size = 1
# node = Q.popleft() -> node = 1
# node.next = Q[0] -> 1.next = None（因为1是最后一个节点）
# Q.append(1.left) -> Q = deque([2])（加入左子节点2）
# Q.append(1.right) -> Q = deque([2, 3])（加入右子节点3）

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

        # 初始化队列，同时将第一层节点加入到队列中，即根节点
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
        