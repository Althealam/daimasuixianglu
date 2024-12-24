# 方法：迭代法
# 思路：将插入节点的值与根节点比较即可，然后插入到叶子结点下面即可，这是最简单的方法
# 时间复杂度：取决于树的高度
# 1. 平衡树：O(logn)
# 2. 不平衡树：O(n)
# 空间复杂度：取决于变量的使用情况
# 1. 变量cur和parent的使用的空间是常数级别的，不会随着n的增加而增加
# 综上，空间复杂度为O(1)

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
        if root is None:
            node=TreeNode(val)
            return node
        
        cur=root
        parent=root
        while cur is not None:
            parent=cur
            if cur.val>val:
                cur=cur.left
            else:
                cur=cur.right
        
        node=TreeNode(val)
        if val<parent.val:
            parent.left=node # 将新节点连接到父结点的左子树
        else:
            parent.right=node # 将新节点连接到父节点的右子树
        
        return root