# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 迭代法
# 遍历二叉树，找到该val对应的节点应该落在的叶子节点位置

# 时间复杂度：
# 1. 二叉树是平衡的：O(logn)
# 2. 二叉树是不平衡的，退化为链表：O(n)
# 空间复杂度：O(1)

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            node=TreeNode(val)
            return node
        
        cur=root
        parent=None
        while cur:
            parent=cur
            if cur.val>val:
                cur=cur.left
            elif cur.val<val:
                cur=cur.right
        
        node=TreeNode(val)
        if parent.val>val:
            parent.left=node
        elif parent.val<val:
            parent.right=node

        return root
        
