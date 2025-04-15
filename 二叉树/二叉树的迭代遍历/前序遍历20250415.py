# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack=[root]
        result=[] # 前序遍历的结果
        while stack:
            node=stack.pop() # 弹出元素
            # 中节点放进去
            result.append(node.val)
            # 右孩子
            if node.right:
                stack.append(node.right)
            # 左孩子
            if node.left:
                stack.append(node.left)
        return result