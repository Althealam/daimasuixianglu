# 方法：动态规划
# 1. dp数组：dp[i]表示以nums[i]为结尾（包括下标i）的最大连续子序列的和为dp[i]
# 2. 递推公式：
# dp[i]=max(dp[i-1]+nums[i],nums[i])
# (1)将nums[i]加入当前连续子序和
# (2)从头开始计算当前连续子序列和
# 3. dp数组的初始化：dp[i]依赖于dp[i-1]
# dp[0]=nums[0]
# 4. 遍历顺序：从前向后

# 时间复杂度：O(n)
# 空间复杂度：O(n)
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp=[0]*len(nums)
        dp[0]=nums[0]
        result=dp[0]
        for i in range(1,len(nums)):
            dp[i]=max(dp[i-1]+nums[i],nums[i])
            result=max(result,dp[i])
        return result
