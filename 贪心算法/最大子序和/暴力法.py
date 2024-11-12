# 方法：暴力法
# 时间复杂度：
# 1. 外层循环遍历nums数组，每次从位置i开始寻找子数组的最大和
# 2. 内层循环对于每一个起点i，计算从i到j的子数组的和
# 总时间复杂度为O(n^2)
# 空间复杂度：
# 只使用了常数级别的变量result和count来存储最大和和当前子数组的和
# 总空间复杂度为O(1)
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result=float('-inf') # 初始化结果为负无穷大
        count=0
        for i in range(len(nums)):
            count=0
            for j in range(i,len(nums)): # 从起始位置i开始遍历寻找最大值
                count+=nums[j]
                result=max(count,result) # 更新最大值
        return result