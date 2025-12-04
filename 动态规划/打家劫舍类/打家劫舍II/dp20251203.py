# 为什么一定是求这两个数组？因为需要确保首尾两个房屋不会被一起偷，因此如果首房子被偷了，尾巴房子就不能被偷，反之同理。因此首房子和尾巴房子只有可能有一个被偷。
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        s1 = self.steal(nums[1:])
        s2 = self.steal(nums[:-1])
        return max(s1, s2)
    
    def steal(self, nums):
        dp = [0]*len(nums)
        if len(nums)==1:
            return nums[0]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[-1]