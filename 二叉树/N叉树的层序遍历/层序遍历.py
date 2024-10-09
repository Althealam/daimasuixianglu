"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val # 节点的值
        self.children = children # 子节点列表
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        # 初始化一个空列表result，用于存储每一层的节点值
        result=[] 
        # 使用collections.deque创建一个双端队列queue，并且初始化为包含根节点
        # deque是一个高效的队列数据结构，支持在两端快速添加和移除元素
        queue=collections.deque([root])

        # 层次遍历循环
        while queue:
            # 获取当前队列的长度，即当前层级的节点数
            level_size=len(queue)
            # 初始化一个空列表level，用于存储当前层级的节点值
            level=[]

            # 遍历当前层级的每个节点
            for _ in range(level_size):
                # 从队列的左侧移除一个节点，并将其赋给node
                node=queue.popleft()
                # 将当前节点的值添加到level列表中
                level.append(node.val)

                # 遍历当前节点的所有子节点
                for child in node.children:
                    # 将每个子节点添加到队列的右侧
                    queue.append(child)
            
            # 将当前层级的节点值列表level添加到result列表中
            result.append(level)

        return result

        