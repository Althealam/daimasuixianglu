# 方法：迭代法
# 时间复杂度：O(n)
# 1. 树的遍历：代码使用了迭代的深度优先搜索（DFS）遍历。每个节点都会被访问一次，并且对每个节点进行了常数次的操作。
# 2. 单个结点的处理：对每个节点，进行的操作包括判断是否为叶子节点、路径和比较、将子节点压入栈等，所有这些操作的复杂度都是常数级别的O(1)
# 空间复杂度：最坏情况下为O(n)，最好情况下为O(logn)
# 1. 栈空间：空间复杂度主要取决于栈的最大深度。在深度优先搜索（DFS）中，栈的最大深度取决于树的高度 H。
# （1）平衡二叉树，高度为logn
# （2）退化树（链式结构），高度为n
# 2. 额外空间：除了栈之外，该算法没有使用额外的数据结构，所有的路径和信息都在栈中存储，因此不需要额外的空间。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if root is None:
            return False
        # 此时栈里放的是pair<节点指针，路径数值>
        st=[(root,root.val)]
        while st:
            node,path_sum=st.pop()
            # 如果该节点是叶子结点，并且该节点的路径数值等于sum，那么就返回true
            if not node.left and not node.right and path_sum==targetSum:
                return True
            # 右节点，压进去一个结点的时候，将该节点的路径数值也记录下来
            if node.right:
                st.append((node.right,path_sum+node.right.val))
            # 左节点
            if node.left:
                st.append((node.left,path_sum+node.left.val))
        return False