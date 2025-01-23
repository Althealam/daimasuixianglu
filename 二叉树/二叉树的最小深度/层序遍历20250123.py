# 思路：本题也是层序遍历的解法。不一样的时候，当遍历到某个节点的左右孩子都为空的时候，就是遍历到最低点了
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        min_depth=0
        queue=collections.deque([root])
        while queue:
            min_depth+=1
            for _ in range(len(queue)):
                node=queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if not node.right and not node.left:
                    return min_depth
        return min_depth

        