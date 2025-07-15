# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 遍历顺序：右中左 
# 递归遍历，先遍历右子树，再对中间节点进行处理，最后遍历左子树
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = []
        cur = root
        pre = 0
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.right
            else:
                cur = stack.pop()
                cur.val+=pre
                pre = cur.val
                cur = cur.left
        return root
