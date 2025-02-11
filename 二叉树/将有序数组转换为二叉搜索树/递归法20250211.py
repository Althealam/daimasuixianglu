# 思路：
# 1. 找到中间节点，中间节点作为root，并记录index
# 2. 分割数组nums为左数组和右数组
# 3. 继续递归处理root的左子树和右子树

# 时间复杂度：O(n)
# 核心思路是每次选取数组的中间元素作为根节点，递归处理左半部分数组和右半部分数组来构建左子树和右子树
# 空间复杂度：O(n)
# 1. 递归调用栈的空间：O(logn)，对于平衡二叉树来说是logn
# 2. 存储二叉搜索树节点的空间：每个节点需要空间进行存储，因此是O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        # 判断数组是否为空
        if not nums:
            return None

        # 找到中间节点的索引
        index=len(nums)//2

        # 构建根节点
        root=TreeNode(nums[index])

        # 构建左子树
        if index>=1:
            left_nums=nums[:index] # 注意[:index]是左闭右开的
            root.left=self.sortedArrayToBST(left_nums)
        # 注意这里不能使用elif，因为if和elif会将左子树和右子树的构建关联起来，导致右子树无法成功构建
        # if和elif是二选一的情况，不是两个都进行

        # 构建右子树
        if index+1<=len(nums)-1:
            right_nums=nums[index+1:]
            root.right=self.sortedArrayToBST(right_nums)
        return root
        