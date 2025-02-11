# 思路：可以只插入到空节点处，也就是让新的节点成为叶子节点
# 前序遍历
# 1. root的值大于val：val应该放在左子树
# 2. root的值小于val：val应该放在右子树
# 3. root为空值：遇到了需要放置新节点的位置

# 时间复杂度：
# 插入操作的时间复杂度取决于二叉搜索树的高度h。在插入新节点时，需要从根节点开始，根据节点值的大小不断向下查找合适的插入位置
# 最好情况：h=logn, O(logn)
# 最坏情况：h=n, O(n)

# 空间复杂度：
# 取决于递归调用栈的深度，并且和树的高度有关
# 最好情况：h=logn, O(logn)
# 最坏情况：h=n, O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        # 中
        if root is None:
            node=TreeNode(val)
            return node
        
        # 左
        # root的值大于val，说明val应该放在root的左边
        if root.val>val:
            root.left=self.insertIntoBST(root.left, val)
        # 右
        # root的值小于val，说明val应该放在root的右边
        elif root.val<val:
            root.right=self.insertIntoBST(root.right, val)
        return root

        