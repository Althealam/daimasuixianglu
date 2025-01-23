"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        result=[]
        queue=collections.deque([root])
        while queue:
            level=[]
            size=len(queue)
            for _ in range(size):
                node=queue.popleft()
                level.append(node.val)
                for child in node.children:
                    queue.append(child)
            result.append(level)
        return result
            

        