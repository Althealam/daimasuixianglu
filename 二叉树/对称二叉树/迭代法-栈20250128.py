# 方法：迭代法
# 时间复杂度：O(n)
# 空间复杂度：O(n)，取决于栈st的大小。最坏情况下，二叉树为完全二叉树，这时候底层的节点数最多，栈会存储n/2个节点。
# 平均情况下，二叉树是平衡二叉树，树的高度是h=logn

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
        st=[] # 使用栈来记录节点
        if root.left:
            st.append(root.left)
        if root.right:
            st.append(root.right)
        while st:
            rightNode=st.pop()
            leftNode=st.pop()
            # 左右孩子节点都为空
            if not rightNode and not leftNode:
                continue
            if not leftNode or not rightNode or leftNode.val!=rightNode.val:
                return False
            st.append(leftNode.left)
            st.append(rightNode.right)
            st.append(leftNode.right)
            st.append(rightNode.left)
        return True
