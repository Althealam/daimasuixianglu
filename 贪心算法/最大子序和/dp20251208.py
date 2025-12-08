# 1. definition: dp[i] is the largest sum of subarray in the nums[:i]
# 2. formula:
# dp[i] = max(dp[i-1]+nums[i], nums[i])
# 3. initialization: dp = [0]*len(nums)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        dp[0] = nums[0]
        res = dp[0] # cannot set res = float('-inf'), otherwise we can not compare dp[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            res = max(res, dp[i])
        return res if res!=float('-inf') else 0