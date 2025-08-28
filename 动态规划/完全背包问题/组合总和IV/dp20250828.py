# 1. dp数组以及下标的含义：dp[j]表示总和为j的元素组合的个数为dp[j]
# 2. 递推公式：
# （1）使用nums[i]: dp[j-nums[i]]
# （2）不使用nums[i]: dp[j]
# 3. 初始化：dp[0] = 1
# 4. 遍历顺序：求排列数，先背包后物品
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0]*(target+1)
        dp[0] = 1
        for i in range(target+1):
            for j in range(len(nums)):
                if i>=nums[j]:
                    dp[i]+=dp[i-nums[j]]
        return dp[-1]
        