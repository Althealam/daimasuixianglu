# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 思路：利用中序遍历，获取二叉搜索树的中序数组，判断中序数组是否是递增的
# 时间复杂度：O(n)
# 1. 中序遍历：O(n)
# 2. 数组比较：O(n)

# 空间复杂度：O(n)
# 1. 递归调用栈：traversal是递归函数，递归调用会使用系统栈空间，最坏情况下二叉树退化为链表，此时递归的深度为n O(n)
# 2. 存储中序遍历结果的数组：O(n)

class Solution:
    def __init__(self):
        self.vec=[]
    
    def traversal(self, node):
        if node.left:
            self.traversal(node.left)
        self.vec.append(node.val)
        if node.right:
            self.traversal(node.right)
        return self.vec

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.vec=self.traversal(root)
        if len(self.vec)==1 or len(self.vec)==0:
            return True
        for i in range(1, len(self.vec)):
            if self.vec[i]<=self.vec[i-1]:
                return False
        return True


        