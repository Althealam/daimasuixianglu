
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.compare(root.left, root.right)

    def compare(self, left, right):
        if left is None or right is None:
            return left is right
        return left.val==right.val and self.compare(left.left, right.right) and self.compare(left.right, right.left)
