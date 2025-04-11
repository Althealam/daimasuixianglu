# 注意：本题也可以用贪心算法解决
# 1. dp数组以及下标的含义：dp[i]表示包含下标i（以nums[i]为结尾的）的最大连续子序列和为dp[i]
# 2. 递推公式：dp[i]=max(dp[i-1]+nums[i], nums[i])
# 3. 初始化：dp[i]是由dp[i-1]推导出来的 dp[0]=nums[0]
# 4. 遍历顺序：从前向后遍历

# 时间复杂度：O(n)
# 空间复杂度：O(n)

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 需要保证子数组至少包含一个元素，因此当长度为1的时候直接返回nums[0]
        if len(nums)==1:
            return nums[0]
        dp=[0]*(len(nums))
        dp[0]=nums[0]
        result=nums[0]
        for i in range(1, len(nums)):
            dp[i]=max(dp[i-1]+nums[i], nums[i])
            if dp[i]>result:
                result=dp[i]
        return result 
