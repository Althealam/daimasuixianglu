# 方法：迭代法
# 左叶子定义：左右孩子为空时，是叶子结点；

# 时间复杂度：O(n)，每个节点会被访问一次
# 空间复杂度：最坏情况下为O(n)（树呈现链状，退化成一条线，递归的深度等于树的高度）；平衡二叉树时，树的高度为logn，此时为O(logn)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0
        st=[root]
        result=0
        while st:
            node=st.pop()
            if node.left and node.left.left is None and node.left.right is None:
                result+=node.left.val
            if node.right:
                st.append(node.right)
            if node.left:
                st.append(node.left)
        return result