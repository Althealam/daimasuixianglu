# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack=[root]
        result=[]
        while stack:
            node=stack.pop()
            # 中节点
            result.append(node.val)
            # 左节点
            if node.left:
                stack.append(node.left)
            # 右节点
            if node.right:
                stack.append(node.right)
        return result[::-1]