# 方法：迭代法（层序遍历）
# 思路：层层遍历每个节点，判断是否是左叶子
# 左叶子的定义：节点A的左孩子不为空，并且该左孩子的左右孩子都为空，可以判断节点A的左孩子为左叶子

# 时间复杂度：O(n) 每个节点都会被访问并且仅仅访问一次
# 空间复杂度：O(n) 层序遍历用队列来辅助实现，并且队列最多会同时存储二叉树每一层的所有节点
# 最坏情况下，二叉树是完全二叉树，最后一层的节点数为n/2，此时的空间复杂度为O(n)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0
        queue=collections.deque([root])
        sum_value=0 # 用来统计左叶子节点之和
        while queue:
            node=queue.popleft()
            if node.left:
                if node.left.left is None and node.left.right is None:
                    sum_value+=node.left.val
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return sum_value
