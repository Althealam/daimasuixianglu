# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 时间复杂度：O(n*d)，n是二叉树的节点总数，d是树的深度
# 1. 通过回溯遍历每个节点 时间复杂度为O(n)
# 2. 对于每个叶子节点，调用get_sum计算其路径之和，因此时间复杂度为O(d)
# 空间复杂度：O(n)

class Solution:
    def __init__(self):
      self.res = 0
      
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
      path = []
      self.traversal(root,path)
      return self.res
    
    def traversal(self, root, path):
      if not root:
        return 0
      path.append(root.val)
      if root.left is None and root.right is None:
        self.res+=self.get_sum(path)
      if root.left:
        self.traversal(root.left, path)
        path.pop()
      if root.right:
        self.traversal(root.right, path)
        path.pop()
      
    def get_sum(self, path):
      s = 0
      for num in path:
        s = s*10+num
      return s
