# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 思路：后序遍历
# 终止条件：当到达叶子节点，则返回None；如果root等于p或者q，则返回root
# 递推：递归左子节点，返回值记录为left；递归右子节点，返回值记录为right
# 返回值：假设返回值为left和right，表示p和q是否在子树中
# 1. left和right同时为空：说明root的左右子树都不包含p和q，返回None
# 2. left和right同时不为空：说明p和q分别在root的两侧，则root为p和q的最近公共祖先
# 3. left为空，right不为空：p和q都不在root的左子树中，返回right
# 4. left不为空，right为空：p和q都不在root的右子树中，返回left

# 时间复杂度：O(n)
# 空间复杂度：O(n)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root is p or root is q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left is None and right is None:
            return None
        elif left is not None and right is None:
            return left
        elif left is None and right is not None:
            return right
        elif left is not None and right is not None:
            return root