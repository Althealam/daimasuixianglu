# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 1. if root==p or root==q: return root
# 2. if left is None and right is None: return None
# 3. if left is not None and right is None: return left
# 4. if left is None and right is not None: return right
# 5. if left is not None and right is not None: return root
# 前序遍历
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root is p or root is q:
            return root
        # 前序遍历 先判断当前节点 再找左右子树
        # 判读是否找到了p或者q节点；如果没有找到p或者q节点的话，判断一下当前遍历的节点是否是祖先节点
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
        