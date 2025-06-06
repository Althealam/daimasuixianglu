from collections import deque
# 定义二叉树节点类
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 辅助函数：将列表转换为二叉树（通过层路遍历将列表转换为二叉树，每次遍历一个节点就把一个节点放到队列里，然后弹出队列的元素并且依次添加其孩子节点（每次弹出一个节点的同时找到其孩子节点）
def list_to_tree(lst):
    if not lst:
        return None
    # 加入根节点
    root = TreeNode(lst[0])
    # 用队列来存储二叉树层序遍历的节点值
    queue = deque([root])
    i = 1
    # 开始依次遍历列表的值，来用层序遍历构建二叉树（感觉可以参考二叉树的层序遍历部分，是两个部分的相反方向，一个是输出层序遍历数组，一个是根据层序遍历数组构建二叉树）
    while queue and i < len(lst):
        node = queue.popleft()
        if lst[i] is not None:
            node.left = TreeNode(lst[i])
            queue.append(node.left)
        i += 1
        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            queue.append(node.right)
        i += 1
    return root

# 层序遍历输出二叉树的值
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result=[]
        queue=collections.deque([root]) # 用来存元素的队列
        while queue: 
            level=[] # 该层的元素值
            for _ in range(len(queue)):
                cur=queue.popleft()
                level.append(cur.val)
                # 开始放入孩子节点，注意不是放入孩子节点的值，而是放入节点
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            result.append(level) 
        return result       