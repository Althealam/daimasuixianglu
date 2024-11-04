# 方法：迭代法
# 思路：如果遍历的根节点比p和q都大的话，说明公共祖先在所遍历的左子树中；如果遍历的根节点比p和q都小的话，说明公共祖先在所遍历的右子树汇总；如果根节点在p和q之间的话，说明该节点就是公共祖先（并且一定是最近的公共祖先）

# 时间复杂度：O(h)，h是二叉搜索树的高度
# 1. 每次递归调用都会根据当前节点的值和目标节点p和q的值来选择遍历左子树和右子树
# 2. 最好情况下，公共祖先是根节点，此时为O(1)；最坏情况下（树为不平衡的链表），递归的深度回达到树的高度h，则时间复杂度为O(h)
# 空间复杂度：O(h)
# 1. 递归实现，空间复杂度取决于递归调用栈的深度
# 2. 最坏情况下，递归栈深度达到树的高度h

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
        while root:
            if root.val>p.val and root.val<q.val:
                root=root.left
            elif root.val<p.val and root.val<q.val:
                root=root.right
            else:
                return root
        return None
        