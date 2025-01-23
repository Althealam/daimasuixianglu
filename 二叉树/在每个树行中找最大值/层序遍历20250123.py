# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        result=[]
        queue=collections.deque([root])
        while queue:
            # inf表示无穷大
            # -inf表示无穷小
            level_max=float('-inf')
            for _ in range(len(queue)):
                node=queue.popleft()
                if node.val>level_max:
                    level_max=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_max)
        return result
                
        