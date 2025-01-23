# 思路：遍历每一层的时候，记录每一层的第一个节点，然后让这一层的第一个节点依次指向本层的最后一个节点
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        queue=collections.deque([root])
        while queue:
            cur=None # 本层的起始节点
            for _ in range(len(queue)):
                node=queue.popleft()
                if cur:
                    cur.next=node
                cur=node # 移动目前的节点到下一个节点（如果是本层的第一个节点，那么会由None变成本层的第一个节点）
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root
