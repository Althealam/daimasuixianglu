# 方法：广度优先搜索（BFS）
# 广度优先搜索从一个节点开始，先访问所有相邻的节点，然后再依次访问每个相邻节点的相邻节点
# 二叉树的层序遍历就是图论中的广度优先搜索在二叉树中的应用
# 时间复杂度：O(n)，其中n是二叉树的节点数
# 1. 节点访问：在广度优先搜索过程中，每个节点会被访问一次，因此对于有n个节点的二叉树，这意味着算法需要访问n个节点
# 2. 操作次数：在遍历过程中，每个节点都会被出队、检查并可能入队其子节点，这些操作对于每个节点来说都是常数时间的操作
# 空间复杂度：O(n)，其中n是二叉树的节点数
# 1. 队列存储：在最坏的情况下，队列可能需要存储所有层的节点。对于一个完全二叉树，队列中的节点数最多等于树的最大宽度，这个在最坏情况下是O(n)
# 2. 节点存储：队列可能同事存储从根节点到当前层的所有节点
# 3. 递归栈：如果使用递归实现BFS，递归栈的深度最多为树的高度，对于一个完全二叉树，递归栈的深度是O(logn)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        depth=0
        queue=collections.deque([root])

        while queue:
            depth+=1
            for _ in range(len(queue)):
                node=queue.popleft()

                if not node.left and not node.right:
                    return depth
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth