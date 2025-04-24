# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 时间复杂度：O(n)
# 1. 中序遍历：O(n)
# 2. 计算最小差值：O(n)

# 空间复杂度：O(n)
# 1. 递归调用栈：递归调用栈的空间复杂度取决于二叉搜索树的高度，最坏情况下二叉树退化为链表，树的高度为n，平均情况为logn 
# 2. 存储节点值的列表：O(n)

class Solution:
    def __init__(self):
        self.nums=[]

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return None
        self.dfs(root, self.nums)
        if len(self.nums)==1:
            return nums[0]
        result=float('inf')
        for i in range(1, len(self.nums)):
            result=min(result, self.nums[i]-self.nums[i-1])
        return result
    
    def dfs(self, node, nums):
        if node.left:
            self.dfs(node.left, nums)
        nums.append(node.val)
        if node.right:
            self.dfs(node.right, nums)

        