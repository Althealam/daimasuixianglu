# nums=list(map(int, input().split()))
# target=int(input())
# 1. dp数组以及下标的含义：dp[i][j]表示使用nums中[0,i]的物品，可以达到总和为target的组合数
# 2. 递推公式：
# （1）不考虑nums[i]（j<nums[i]）：dp[i-1][j]
# （2）考虑nums[i]（j>=nums[i]）：dp[i-1][j]+dp[-1][j-nums[i]]
# 3. 初始化：dp=[[0]*(target+1) for _ in range(len(nums))]
# dp[i][0]=1
# dp[0][j]不可以进行初始化，因为依赖于dp[-1][j-nums[0]]
# 4. 遍历顺序：先背包，后物品


class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp=[[0]*(target+1) for _ in range(len(nums))]
        for i in range(len(nums)):
            dp[i][0]=1
        for j in range(1, target+1): # 遍历背包
            for i in range(len(nums)): # 遍历物品
                if j>=nums[i]:
                    dp[i][j]=dp[i-1][j]+dp[-1][j-nums[i]]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[-1][-1]

            
