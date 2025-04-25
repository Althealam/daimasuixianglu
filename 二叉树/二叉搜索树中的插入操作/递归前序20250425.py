# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 如果val>root.val：则val放在root.right
# 2. 如果val<root.val：则val放在root.left
# 3. 如果root is None：node=TreeNode(val)
# 前序遍历

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # 中节点
        if root is None:
            node=TreeNode(val)
            return node
        
        # 判断
        if val>root.val:
            root.right=self.insertIntoBST(root.right, val)
        elif val<root.val:
            root.left=self.insertIntoBST(root.left, val)
        
        return root

        