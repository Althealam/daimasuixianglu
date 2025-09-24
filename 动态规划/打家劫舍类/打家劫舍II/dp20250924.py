class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return 1
        case1 = self.steal(nums[1:])
        case2 = self.steal(nums[:-1])
        return max(case1, case2)
    
    def steal(self, nums):
        if len(nums)==1:
            return nums[0]
        if len(nums)==0:
            return 0
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[-1]