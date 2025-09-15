# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            node = TreeNode(val = val)
            return node
        
        cur = root
        parent = cur
        while cur:
            parent = cur
            if cur.val>val:
                cur = cur.left
            elif cur.val<val:
                cur = cur.right
        
        node = TreeNode(val)
        if parent.val>val:
            parent.left = node
        elif parent.val<val:
            parent.right = node
        return root
        