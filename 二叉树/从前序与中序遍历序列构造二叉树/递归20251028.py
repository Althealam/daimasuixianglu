# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder)==0 or len(inorder)==0:
            return None
        root_val = preorder[0]
        root = TreeNode(root_val)
        inorder_index = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:inorder_index+1], inorder[:inorder_index])
        root.right = self.buildTree(preorder[inorder_index+1:], inorder[inorder_index+1:])
        return root