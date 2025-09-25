# 1. dp数组以及下标的含义：dp[i]表示以nums[i]为结尾的最长递增子序列的长度
# 2. 递推公式：nums[i]>nums[j]: dp[i] = dp[j]+1
# 3. 初始化：全部初始化为1
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        res = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[j]+1, dp[i])
                res = max(res, dp[i])
        return res
        