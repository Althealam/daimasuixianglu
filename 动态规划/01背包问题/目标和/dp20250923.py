# 1. dp数组以及下标的含义：满足加法总和值为i的方法数为dp[i]
# 2. 递推公式：dp[j]+=dp[j-nums[i]]
# x1+x2 = sum(nums) x1-x2 = target ==> x1 = (sum(nums)+target)//2
# 3. 初始化：dp=[0]*(target+sum+1)
# 4. 遍历顺序：先物品后背包 背包逆序
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if (sum(nums)+target)%2!=0:
            return 0
        if len(nums)==0:
            return 0
        target_sum = (sum(nums)+target)//2
        if target_sum<0:
            return 0
        dp = [0]*(target_sum+1)
        dp[0] = 1
        for i in range(len(nums)):
            for j in range(target_sum, -1, -1):
                if j>=nums[i]:
                    dp[j]+=dp[j-nums[i]]
        return dp[-1]
        