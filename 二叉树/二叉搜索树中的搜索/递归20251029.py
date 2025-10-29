# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# judge this node:
# 1. if node.val==val: return node
# 2. elif node.val>val: the finding node is on the left of the node
# 3. elif node.val<val: the finding node is on the right of the node 
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == val:
            return root
        elif root.val>val:
            return self.searchBST(root.left, val)
        elif root.val<val:
            return self.searchBST(root.right, val)
        
        