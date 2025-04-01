# 1. dp数组以及下标的含义：dp[j]表示组成正整数j的组合个数有dp[j]个（本题是求解排列数，也就是112和211不同）
# 2. 递推公式：
# dp[j]+=dp[j-nums[i]]
# 3. 初始化：全部初始化为0，dp[0]=1
# 4. 遍历顺序：先背包，后物品

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp=[0]*(target+1)
        dp[0]=1
        for j in range(target+1): # 遍历背包
            for i in range(len(nums)): # 遍历物品
                if j>=nums[i]:
                    dp[j]+=dp[j-nums[i]]
        return dp[target]
        