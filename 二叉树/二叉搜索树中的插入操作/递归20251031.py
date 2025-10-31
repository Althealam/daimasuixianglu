# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None: # already achieve the place we need to put our node
            node = TreeNode(val)
            return node
        if root.val>val: # val should be in the left of the root
            root.left= self.insertIntoBST(root.left, val)
        elif root.val<val:
            root.right= self.insertIntoBST(root.right, val)
        
        return root