# 1. dp数组以及下标的含义：dp[i]表示从[0, i-1]内连续子数组的最大和为dp[i]
# 2. 递推公式：
# （1）重新开始：nums[i]
# （2）不重新开始：dp[i-1]+nums[i]
# 3. 初始化：dp[0] = nums[0]
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], dp[i])
        return max(dp)