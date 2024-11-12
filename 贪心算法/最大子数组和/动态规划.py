# 方法：动态规划

# 时间复杂度：从索引1到len(nums)-1的for循环，在循环中更新dp[i]和res都是常数时间操作
# 总的时间复杂度为O(n)
# 空间复杂度：使用了一个大小为len(nums)的数组dp来存储每个位置的最大子数组和
# 总的空间复杂度为O(n)
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp=[0]*len(nums)
        dp[0]=nums[0]
        res=nums[0]
        for i in range(1,len(nums)):
            dp[i]=max(dp[i-1]+nums[i],nums[i])
            res=max(res,dp[i])
        return res