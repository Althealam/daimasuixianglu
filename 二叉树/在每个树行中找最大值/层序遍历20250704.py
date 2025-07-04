# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        result= []
        if not root:
            return []
        queue = collections.deque([root])
        while queue:
            level_max_node = float('-inf')
            for _ in range(len(queue)):
                node = queue.popleft()
                level_max_node = max(node.val, level_max_node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_max_node)
        return result