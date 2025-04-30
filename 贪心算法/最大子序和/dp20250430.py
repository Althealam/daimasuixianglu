# 1. dp数组以及下标的含义：dp[i]表示从[0, i-1]的nums数组的最大子数组和
# 2. 递推公式：
# （1）重新开始：nums[i]
# （2）不重新开始：dp[i-1]+nums[i]
# 3. 初始化：全部初始化为0 dp[0]=nums[0]
# 4. 遍历顺序：从左到右遍历
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 需要保证子数组内至少有一个元素
        if len(nums)==1:
            return nums[0]
        dp=[0]*len(nums)
        dp[0]=nums[0]
        result=float('-inf') # 记录最大子数组和
        for i in range(len(nums)):
            dp[i]=max(dp[i-1]+nums[i], nums[i])
            result=max(dp[i], result)
        return result

