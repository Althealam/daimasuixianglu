# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 后序遍历：根据p和q的节点值来找最近公共祖先
# 1. 递归的终止条件：root等于p或者q；root为空
# 2. 递归：先求解左右子树
# 中节点：如果root.val>p.val：p在root的左子树；如果root.val<p.val：p在root的右子树
# 3. 二叉搜索树的最近公共祖先：祖先值刚好在p和q之间

# 时间复杂度：O(n)，其中n是二叉搜索树的节点个数
# 空间复杂度：O(1)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ancestor=root
        while True:
            if root.val>p.val and root.val>q.val:
                root=root.left
            elif root.val<p.val and root.val<q.val:
                root=root.right
            else:
                return root
        return None