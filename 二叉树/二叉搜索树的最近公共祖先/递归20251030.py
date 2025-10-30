# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# find the ancestor of binary search tree
# 1. if root.val<p.val and root.val<q.val: find the ancestor in root.right
# 2. elif root.val>p.val and root.val>q.val: find the ancestor in root.left
# 3. else: return root
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val<p.val and root.val<q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val>p.val and root.val>q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root
        
    