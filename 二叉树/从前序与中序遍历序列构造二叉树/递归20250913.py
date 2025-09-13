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
        node = TreeNode(val = preorder[0])
        node_index = inorder.index(node.val)
        node.left = self.buildTree(preorder[1:node_index+1], inorder[:node_index])
        node.right = self.buildTree(preorder[node_index+1:], inorder[node_index+1:])
        return node
        