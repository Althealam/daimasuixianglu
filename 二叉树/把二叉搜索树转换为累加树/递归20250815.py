# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 遍历顺序：右中左
# 递归遍历：先遍历右子树，再对中间节点进行处理，最后遍历左子树

# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def __init__(self):
      self.pre = TreeNode(val=0)
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
      if not root:
        return None
      if root.right:
        root.right = self.convertBST(root.right)
      root.val+=self.pre.val
      self.pre = root
      if root.left:
        root.left = self.convertBST(root.left)
      return root