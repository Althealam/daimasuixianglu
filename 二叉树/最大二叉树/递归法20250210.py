# 思路：
# 1. 判断nums是否为空，如果是的话则直接返回空数组
# 2. 找到nums中的最大值，分割数组为左数组和右数组，并且设置根节点的值为最大值
# 3. 依次类推找到root.left和root.right

# 时间复杂度：O(n^2)
# 1. 第一次递归：遍历长度为n的数组来找到最大值，此时的时间复杂度为O(n)
# 2. 第二次递归：递归构建左子树和右子树，，每次递归调用中查找最大值的时间复杂度依次为O(n), O(n-1), ... , O(1)
# 总结的时间复杂度为：O(n)+O(n-1)+...+O(1)=O(n^2)

# 空间复杂度：由递归调用栈的深度决定
# 1. 最坏情况下，输入数组是有序的，构建出来的最大二叉树退化为一个链表，此时的复杂度为O(n)
# 2. 平均情况下，树的高度为O(logn)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        if not nums:
            return []
        # 2. 寻找数组最大值
        max_num=float('-inf')
        max_num_index=0
        for index, item in enumerate(nums):
            if item>max_num:
                max_num=item
                max_num_index=index
        # 3. 设置root的节点值
        root=TreeNode(val=max_num)

        # 注意：需要判断max_num_index是否满足条件
        # 4. 切割数组并递归构造左右子树
        if max_num_index>0:
            left_nums=nums[0:max_num_index]
            root.left=self.constructMaximumBinaryTree(left_nums)
        if max_num_index<len(nums)-1:
            right_nums=nums[max_num_index+1:]
            root.right=self.constructMaximumBinaryTree(right_nums)
        return root