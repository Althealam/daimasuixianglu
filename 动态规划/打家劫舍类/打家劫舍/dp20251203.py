# 1. definition: dp[i] means the maximal amount of money you can rob from the house 0 to house i-1
# 2. formula: 
# (1) rob house i-1: dp[i-2]+nums[i] 偷第i-1间
# (2) don't rob house i-1: dp[i-1] # 第i间能偷到的结果就是第i-1间能偷到的最好结果
# dp[j] = max(dp[i-2]+nums[i], dp[i-1])
# 3. initialization: dp[0] = nums[0]
# 4. order: left to right
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        dp[0] = nums[0]
        if len(nums)==1:
            return nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)): # iterate hourse
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[-1]
    