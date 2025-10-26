# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = collections.deque([root])
        min_depth = 0
        while queue:
            min_depth+=1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left is None and node.right is None:
                    return min_depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return min_depth