# 1. dp数组以及下标的含义：dp[i]表示以nums[i]为结尾的最大子数组和
# 2. 递推公式：
# （1）从头开始考虑：nums[i]
# （2）考虑nums[i]：dp[i-1]+nums[i]
# dp[i]=max(dp[i-1], dp[i-1]+nums[i])
# 3. 初始化：dp[0]=nums[0]
# 4. 遍历顺序：从前向后遍历
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp=[0]*len(nums)
        dp[0]=nums[0]
        for i in range(1, len(nums)):
            dp[i]=max(nums[i], dp[i-1]+nums[i])
        return max(dp)


        