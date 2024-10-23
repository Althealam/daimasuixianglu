# 分析：构造二叉树的题目都要用前序遍历（因为先构造中间节点，然后递归构造左子树和右子树）
# 1. 确定递归函数的参数和返回值：参数传入的是存放元素的数组，返回该数组构造的二叉树的头节点，返回类型是指向节点的指针
# 2. 确定终止条件：题目指明了数组大小一定大于等于1，因此当递归遍历时数组大小为1时，说明遍历到叶子结点了
# 3. 确定单层递归的逻辑：
# （1）找到数组中最大的值和对应的下标，最大的值构造根节点，下标用来下一步分隔数组
# （2）最大值所在的下标左区间，构造左子树：需要maxValueIndex>0，因为要保证左区间至少有一个数值
# （3）最大值所在的下标右区间，构造右子树：需要maxValueIndex<num.size()-1，因为要保证右区间至少有一个数值

# 时间复杂度：O(n^2)
# 总共要遍历的时间复杂度：O(n+(n-1)+...+1)=O(n^2)
# 1. 寻找最大值和下标：每次递归中，遍历nums数组中的每个元素找到最大值和下标，这一步的时间复杂度为O(n)
# 2. 递归处理：在找到最大值之后，将数组分为左右两边，并且递归的对左右进行子树的构建。递归过程中，也会有O(n)的最大值查找
# 最坏情况：数组严格递增或者递减，需要递归n层，并且第i层需要遍历n-i个元素以找到最大值，总时间复杂度 为O(n+(n-1)+...+1)=O(n^2)

# 空间复杂度：O(n)，因为递归的深度最坏情况下是n，同时每次调用栈上只需要存储当前的nums切片
# 1. 递归调用栈的深度：在递归中，每次会根据最大值将数组分成左右两部分，并递归处理。最坏情况下，递归的深度为O(n)，即递减序列情况下，树的高度为n，因为每次只能构建一个左子树
# 2. 额外空间：每次递归中，函数会创建新的new_list（左右区间）

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
        if len(nums)==1:
            return TreeNode(nums[0])

        node=TreeNode(0)
        # 找到数组中最大的值和对应的下标
        maxValue=0
        maxValueIndex=0
        for i in range(len(nums)):
            if nums[i]>maxValue:
                maxValue=nums[i]
                maxValueIndex=i
        node.val=maxValue

        # 最大值所在的下标的左区间---构造左子树
        if maxValueIndex>0:
            new_list=nums[:maxValueIndex] # 左闭右开区间
            node.left=self.constructMaximumBinaryTree(new_list)
        # 最大值所在的下标的右区间--构造右子树
        if maxValueIndex<len(nums)-1:
            new_list=nums[maxValueIndex+1:]
            node.right=self.constructMaximumBinaryTree(new_list)

        return node
