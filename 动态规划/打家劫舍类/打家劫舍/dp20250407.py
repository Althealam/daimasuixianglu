# 1. dp数组以及下标的含义：dp[i]表示偷[0,i]的房屋时，可以偷窃到的最高金额是dp[i]
# 2. 递推公式：
# （1）偷i的房间：dp[i]=dp[i-2]+nums[i]
# （2）不偷i的房间：dp[i]=dp[i-1]
# dp[i]=max(dp[i-2]+nums[i], dp[i-1])
# 3. 初始化：全部初始化为0 dp[0]=nums[0] dp[1]=max(nums[0], nums[1])
# 4. 遍历顺序：dp[i]由dp[i-1]和dp[i-2]推出，因此需要从前向后

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        dp=[0]*len(nums)
        dp[0]=nums[0]
        dp[1]=max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i]=max(dp[i-1], dp[i-2]+nums[i])
        return dp[len(nums)-1]
        