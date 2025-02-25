# 1. dp数组以及下标的含义：考虑[0,i]以内的房屋，最多可以偷窃的金额为dp[i]
# 2. 递推公式：dp[i]=max(dp[i-2]+nums[i],dp[i-1])
# （1）如果偷第i个房间：dp[i]=dp[i-2]+nums[i]
# （2）如果不偷第i个房间：dp[i]=dp[i-1]
# 3. 初始化：由递推公式可以知道递推公式的基础是dp[0]和dp[1]
# dp[0]=nums[0], dp[1]=max(nums[0], nums[1])
# 4. 遍历顺序：从前向后遍历

# 时间复杂度：O(n)
# 空间复杂度：O(n)

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 特殊情况
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]

        dp=[0]*len(nums)
        dp[0]=nums[0]
        dp[1]=max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i]=max(dp[i-1], dp[i-2]+nums[i])
        return dp[-1]
        