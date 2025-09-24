# 1. dp数组以及下标的含义：dp[i]表示小偷偷窃[0, i-1]的房屋时能够偷窃到的最高金额
# 2. 递推公式：dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])
# 3. 初始化：dp[0]=nums[0] dp[1] = max(nums[0], nums[1])
# 4. 遍历顺序：从前向后遍历
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        if len(nums)==1:
            return nums[0]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[-1]
        