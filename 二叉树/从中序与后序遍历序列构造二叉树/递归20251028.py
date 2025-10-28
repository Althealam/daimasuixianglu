# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder)==0 or len(postorder)==0:
            return None
        root_val = postorder[-1]
        root = TreeNode(root_val)
        inorder_index = inorder.index(root_val)
        root.left = self.buildTree(inorder[:inorder_index], postorder[:inorder_index])
        root.right = self.buildTree(inorder[inorder_index+1:], postorder[inorder_index:-1])
        return root
        