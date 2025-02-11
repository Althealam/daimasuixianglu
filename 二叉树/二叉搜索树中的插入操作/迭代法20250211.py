# 思路：可以只插入到空节点处，也就是让新的节点成为叶子节点
# 前序遍历
# 1. root的值大于val：val应该放在左子树
# 2. root的值小于val：val应该放在右子树
# 3. root为空值：遇到了需要放置新节点的位置

# 时间复杂度：O(h)
# 空间复杂度：O(1)
# 迭代法的过程中，只使用了cur和parent，不涉及递归调用栈的额外空间开销，因此是O(1)

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
        # 中（根节点为空，找到插入位置）
        if root is None:
            node=TreeNode(val)
            return node
        
        cur=root
        parent=root # 记录上一个节点，用来连接新的节点

        # 遍历查找可以插入的位置
        while cur is not None:
            parent=cur
            # 移动cur节点
            if cur.val>val:
                cur=cur.left
            elif cur.val<val:
                cur=cur.right
        
        # 插入节点
        node=TreeNode(val)
        if val<parent.val:
            parent.left=node # 新节点连接到父节点的左子树
        else:
            parent.right=node # 新节点连接到父节点的右子树
        
        return root