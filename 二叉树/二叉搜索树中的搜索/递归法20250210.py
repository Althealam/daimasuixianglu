# 注意：二叉搜索树BST的特性是，左节点一定小于根节点，右节点一定大于根节点
# 思路：
# 1. 如果root.val>val：查找root.left
# 2. 如果root.val<val：查找root.right
# 3. 如果root.val==val：返回root


# 时间复杂度：O(h)，其中h是二叉搜索树的高度
# 1. 最好情况：二叉树完全平衡
# 2. 最坏情况：二叉树退化为链表
# 空间复杂度：O(h)，递归调用会使用栈来保存

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return []
        
        if root.left and root.val>val:
            return self.searchBST(root.left, val)
        if root.right and root.val<val:
            return self.searchBST(root.right, val)
        if root and root.val==val:
            return root
    