# 方法：迭代法
# 分析：1. 找到要删除的节点 2. 删除节点（删除节点的步骤最麻烦）
# 第一种情况：没有找到要删除的节点--直接返回即可
# 第二种情况：要删除的节点是叶子结点--直接删除即可
# 第三种情况：要删除的节点的左右孩子节点不为空--大幅度修改二叉树的结构，要把左子树放在右子树的最左边节点
# 第四种情况：要删除的节点左孩子节点不为空，右孩子节点为空--直接让要删除的节点的父节点指向左孩子节点
# 第五种情况：要删除的节点左孩子节点为空，右孩子节点为空--直接让要删除的节点的父节点指向右孩子节点

# 时间复杂度：平均情况下为O(logn)，最坏情况下为O(n)
# 空间复杂度：O(1)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteOneNode(self,target):
        """
        将目标接待你的左子树放到目标节点的右子树的最左节点的左孩子位置上
        返回：目标节点右孩子作为新的根节点
        """
        if target is None:
            return target
        if target.right is None:
            return target.left
        cur=target.right
        while cur.left:
            cur=cur.left
        cur.left=target.left
        return target.right

    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return root
        cur=root
        pre=None # 记录cur的父节点，用来删除cur
        while cur:
            if cur.val==key:
                break
            pre=cur
            if cur.val>key:
                cur=cur.left
            else:
                cur=cur.right
        if pre is None:  # 如果搜索树只有头结点
            return self.deleteOneNode(cur)
        # pre 要知道是删左孩子还是右孩子
        if pre.left and pre.left.val == key:
            pre.left = self.deleteOneNode(cur)
        if pre.right and pre.right.val == key:
            pre.right = self.deleteOneNode(cur)
        return root
        