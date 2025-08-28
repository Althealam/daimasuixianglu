# 1. dp数组以及下标的含义：dp[j]表示背包容量为j时能够放下的最大物品价值
# 2. 递推公式
# （1）不放物品i：dp[j]
# （2）放物品i：dp[j-nums[i]]+nums[i]
# 3. 初始化：全部初始化为0
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        target = sum(nums)//2
        dp=[0]*(target+1)
        dp[0] = 0
        for i in range(len(nums)): # 遍历物品
            for j in range(target, -1, -1): # 遍历背包
                if j>=nums[i]:
                    dp[j] = max(dp[j], dp[j-nums[i]]+nums[i])
        if dp[target]==target:
            return True
        return False