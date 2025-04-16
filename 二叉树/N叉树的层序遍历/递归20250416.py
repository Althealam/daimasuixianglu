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
        def traversal(root, depth):
            # 到达新的一层，加入新的空数组
            if len(result)==depth:
                result.append([])
            result[depth].append(root.val)
            # 判断是否有孩子节点
            if root.children:
                # 遍历孩子节点
                for i in range(len(root.children)):
                    traversal(root.children[i], depth+1)
        traversal(root, 0)
        return result

            