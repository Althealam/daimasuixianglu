# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 时间复杂度：O(n)
# 函数会递归遍历二叉树的每个节点恰好一次
# 空间复杂度：O(w)
# 递归调用会使用系统的栈空间
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        if not root:
            return 0
        queue = collections.deque([root])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            max_depth+=1
        return max_depth