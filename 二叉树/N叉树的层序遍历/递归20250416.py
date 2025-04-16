"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        result=[]
        # 递归法
        def traversal(root, depth):
            # 判断是否达到叶子节点
            if len(result)==depth:
                result.append([])
            # 在第depth层加入root的节点值
            result[depth].append(root.val)
            # 加入孩子节点的值
            if root.children:
                for i in range(len(root.children)): # 遍历孩子节点
                    traversal(root.children[i], depth+1)
        traversal(root, 0)
        return result