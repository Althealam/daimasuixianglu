# 1. dp数组以及下标的含义：dp[i]表示以nums[i]为结尾的最长连续递增序列的长度
# 2. 递推公式
# if nums[i]>nums[i-1]: dp[i]=max(dp[i], dp[i-1]+1)
# 3. 遍历顺序：从前向后遍历
# 4. 初始化：dp[0]=1 全部初始化为1

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        dp=[1]*len(nums)
        dp[0]=1
        for i in range(1, len(nums)):
            if nums[i]>nums[i-1]:
                dp[i]=max(dp[i], dp[i-1]+1)
        return max(dp)

        