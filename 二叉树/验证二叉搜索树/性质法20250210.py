# 思路：
# 1. 节点的左子树只包含小于当前节点的数
# 2. 节点的右子树只包含大于当前节点的数
# 3. 所有左右子树也必须是二叉搜索树

# 将二叉搜索树用中序遍历变成数组，然后判断数组是否为递增的，如果不是有序的则返回False

# 时间复杂度：O(n)
# 1. 中序遍历：traversal递归访问二叉树的每个节点，O(n)
# 2. 检查数组有序性：O(n)

# 空间复杂度：O(n)
# 1. 递归调用栈空间：取决于二叉树的高度，O(h)
# 2. 存储中序遍历结果的数组空间：O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        self.vector=[]
        self.traversal(root) # 获取二叉搜索数的中序数组
        for i in range(1,len(self.vector)):
            if self.vector[i-1]>=self.vector[i]:
                return False
        return True

    def __init__(self):
        self.vector=[]

    def traversal(self, root):
        if root is None:
            return
        self.traversal(root.left) # 左
        self.vector.append(root.val)
        self.traversal(root.right) # 右