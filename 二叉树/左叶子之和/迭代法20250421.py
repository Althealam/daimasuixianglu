# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 左叶子的条件：root.left非空&root.left.left是空&root.left.right是空
# 时间复杂度：O(n)，其中n是二叉树节点数量，因为代码需要遍历二叉树的每个节点
# 空间复杂度：O(n)，最坏情况下二叉树退化为链表，栈st最多需要存储n个节点


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        st=[root]
        result=0 # 计算左叶子之和
        while st:
            node=st.pop()
            # 判断为左叶子
            if node.left is not None and node.left.left is None and node.left.right is None:
                result+=node.left.val
            if node.right: # 右节点
                st.append(node.right)
            if node.left: # 左节点
                st.append(node.left)
        return result