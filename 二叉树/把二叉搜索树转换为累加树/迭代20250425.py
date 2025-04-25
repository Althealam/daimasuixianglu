# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 迭代法（二叉树的迭代法都是通过栈来实现的）
# 在处理中节点的时候要进行累加操作


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack=[]
        cur=root
        pre=0
        while cur or stack:
            if cur:
                stack.append(cur)
                cur=cur.right # 右
            else:
                cur=stack.pop() # 中
                cur.val+=pre
                pre=cur.val
                cur=cur.left # 左
        return root
