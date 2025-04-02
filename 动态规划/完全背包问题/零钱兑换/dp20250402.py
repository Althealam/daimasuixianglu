# 1. dp数组以及下标的含义：dp[j]表示凑成金额j的最少的硬币个数是dp[j]
# 2. 递推公式：
# （1）不考虑coin：dp[j]
# （2）考虑coin：dp[j-coin]+1
# dp[j]=min(dp[j], dp[j-coin]+1)
# 3. 初始化：由于求最少的硬币个数，因此所有都初始化为正无穷
# 4. 遍历顺序：本题是求组合数，因此是先物品后背包
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float('inf')]*(amount+1)
        dp[0]=0
        for coin in coins: # 遍历物品
            for j in range(amount+1): # 遍历背包
                if j>=coin:
                    dp[j]=min(dp[j], dp[j-coin]+1)
        return dp[amount] if dp[amount]!=float('inf') else -1

        
        