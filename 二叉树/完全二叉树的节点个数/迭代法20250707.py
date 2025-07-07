# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = collections.deque([root])
        cnt = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                cnt+=1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return cnt