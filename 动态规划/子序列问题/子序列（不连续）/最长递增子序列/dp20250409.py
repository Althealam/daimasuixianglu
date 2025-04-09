# 1. dp数组以及下标的含义：dp[i]表示以nums[i]为结尾的最长递增子序列的长度
# 2. 递推公式
# 位置i的最长递增子序列等于j从0到i-1各个位置的最长递增子序列+1的最大值
# 只要nums[i]>nums[j]，那么nums[i]可以接在0到i-1的最长递增子序列的尾部，从而实现递增子序列长度的增加
# if nums[i]>nunms[j]: dp[i]=max(dp[i], dp[j]+1)
# 3. 初始化：dp[0]=1 dp数组全部初始化为1
# 4. 遍历顺序：从前向后遍历

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[1]*len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i], dp[j]+1)
        return max(dp)
        