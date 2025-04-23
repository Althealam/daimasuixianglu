# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 时间复杂度：O(n) 最坏情况下需要遍历二叉搜索树中的每个节点才能找到
# 空间复杂度：取决于栈的最大深度，栈的最大深度和树的高度有关。最坏情况下，树退化为链表，此时栈的最大深度为n，因此空间复杂度为O(n)
# 平均情况下，二叉树是平衡的，此时树的高度为logn，那么栈的最大深度为O(logn)

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None
        stack=[root]
        while stack:
            node=stack.pop()
            if node.val==val:
                return node
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return None