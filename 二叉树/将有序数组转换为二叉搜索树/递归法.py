# 方法：递归法
# 分析：我们要去寻找中间节点，这样才能保证左区间和右区间的节点数量是相同的，同时对于左右区间，也是去选择中间节点
# 先找到根节点，也就是中间节点，然后再递归构造左右子树即可

# 时间复杂度：O(n)，其中n是nums的长度
# 1. 递归过程中，每个元素都被访问并且用于构造树节点，并且每个元素在递归过程中仅访问一次
# 空间复杂度：O(n)
# 1. 递归调用栈，空间复杂度由递归的深度决定。每次递归调用栈的深度为树的高度，而树的高度为O(logn)，因此空间复杂度为O(logn)
# 2. 算法会构建一个二叉搜索树，其中每个节点对应数组的一个元素，总共会构建n个节点，因此树的节点的空间为O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def traversal(self,nums, left, right):
        if left>right: # 终止条件
            return None
        # 单层递归的逻辑
        mid=(left+right)/2
        # 构造根节点
        root=TreeNode(nums[mid]) 
        # 构造左子树
        root.left=self.traversal(nums,left,mid-1) # 左闭右闭区间
        # 构造右子树
        root.right=self.traversal(nums,mid+1,right) # 左闭右闭区间
        return root
    
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        root=self.traversal(nums,0,len(nums)-1)
        return root
        