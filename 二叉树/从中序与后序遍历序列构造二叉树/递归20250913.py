# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder)==0:
            return None
        root_val = postorder[-1]
        root_inorder_ind = inorder.index(root_val)
        root = TreeNode(val=root_val)
        root.left = self.buildTree(inorder[:root_inorder_ind], postorder[:root_inorder_ind])
        root.right = self.buildTree(inorder[root_inorder_ind+1:], postorder[root_inorder_ind:-1])
        return root