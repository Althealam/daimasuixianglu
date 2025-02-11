# 思路：二叉搜索树是有序的
# 最近公共祖先一定是左子树为p/q，右子树为q/p。那么也就是说，p.val<=root.val<=q.val

# 时间复杂度：O(h)
# 二叉搜索树查找最近公共祖先，实际上是不断根据当前节点的值和目标节点p、q的值的大小关系，来决定是向左子树还是右子树进行递归查找的过程
# 1. 最好情况：二叉树完全平衡，h=logn
# 2. 最坏情况：二叉树退化为链表，h=n

# 空间复杂度：O(h)
# 递归调用栈的深度决定了空间复杂度
# 1. 最好情况：完全平衡，h=logn
# 2. 最坏情况：h=n，二叉树退化为链表

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # 比较root的值和p, q的值的大小
        # 1. 如果root的值大于p和q，说明最近的公共祖先在root的左子树
        if root.val>p.val and root.val>q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # 2. 如果root的值小于p和q，说明最近的公共祖先在root的右子树
        elif root.val<p.val and root.val<q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        # 3. 如果root的值在p和q之间，说明找到了最近的公共祖先
        else:
            return root


        