# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 思路：BFS这棵二叉树，将右儿子入队，再让左儿子入队，这样最后一个出队节点就是左下脚的节点了
# 时间复杂度：O(n)
# 空间复杂度：O(n)
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        while q:
            node = q.popleft()
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
        return node.val