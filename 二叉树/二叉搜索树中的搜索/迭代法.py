# 方法：迭代法
# 二叉搜索树的定义：根节点比左子树大，根节点比右子树小（它的左、右子树也为二叉搜索树）
# 二叉搜索树不需要考虑遍历顺序，并且不需要回溯的过程，因为节点的有序性已经帮我们确定了搜索的方向

# 时间复杂度：代码逐层遍历二叉树，根据 val 与当前节点 root.val 的大小关系，选择继续搜索左子树或右子树。因此，时间复杂度与树的高度成正比：
# 1. 平衡二叉搜索树：
# 在平衡的 BST 中，树的高度为 O(log n)，其中 n 是树中的节点数。因此，平均情况下的时间复杂度为 O(log n)。
# 2. 非平衡二叉搜索树：
# 在最坏情况下，树的高度可能为 O(n)（例如，链状的非平衡树），因此最坏情况下的时间复杂度为 O(n)。
# 空间复杂度：
# 由于是迭代实现，不使用递归，因此无需额外的栈空间来保存递归调用。
# 空间复杂度为常数 O(1)，因为除了指向当前节点的指针 root，没有使用其他额外的空间。


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
        while root!=None:
            if val<root.val:
                root=root.left
            elif val>root.val:
                root=root.right
            else:
                return root
        return None