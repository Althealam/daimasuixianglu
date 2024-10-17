# 方法：迭代法（层次遍历）
# 时间复杂度：O(n)
# 空间复杂度：取决于queue的大小，最坏情况下为O(n)（此时树为完全平衡的二叉树，队列最多的节点出现在树的最后一层），最好情况下为O(1)（此时树是一个链条，队列中最多只会有一个节点）
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections
class Solution(object):
    def countNodes(self,root):
       queue=collections.deque() 
       if root:
            queue.append(root)
       result=0
       while queue:
            size=len(queue)
            for i in range(size):
                node=queue.popleft()
                result+=1 # 记录节点数量
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
       return result