# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []
        self.inorder(root, res)
        for i in range(len(res)):
            if i>0 and res[i]<=res[i-1]:
                return False
        return True

    
    def inorder(self, root, res):
        """
        中序遍历
        """
        if not root:
            return None
        if root.left:
            self.inorder(root.left, res)
        res.append(root.val)
        if root.right:
            self.inorder(root.right, res)