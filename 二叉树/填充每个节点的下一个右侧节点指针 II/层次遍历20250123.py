# 思路：本题和上一题没有区别，只是上一题是完全二叉树，本题不是，但是填充每个节点的右指针的时候其实并不需要是完全二叉树
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
            cur=None
            for _ in range(len(queue)):
                node=queue.popleft()
                if cur:
                    cur.next=node
                cur=node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root

        