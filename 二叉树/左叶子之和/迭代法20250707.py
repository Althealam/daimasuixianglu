# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 注意：不能通过限制i==0来选择左边的节点，因为可能会出现一层里只有一个节点的情况
# 时间复杂度：O(n)，n是二叉树的节点个数
# 空间复杂度：O(w)，其中w是二叉树的最大宽度
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = collections.deque([root])
        ans = 0
        while queue:
            node = queue.popleft()
            # 检查左子节点是否是叶子节点
            if node.left:
                if node.left.left is None and node.left.right is None:
                    ans += node.left.val
                queue.append(node.left)
            # 继续处理右子节点
            if node.right:
                queue.append(node.right)
        return ans
