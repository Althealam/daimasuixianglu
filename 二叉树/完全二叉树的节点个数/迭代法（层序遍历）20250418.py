# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        ans=0
        if not root:
            return 0
        queue=collections.deque([root])
        while queue:
            for _ in range(len(queue)):
                node=queue.popleft()
                ans+=1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans
        