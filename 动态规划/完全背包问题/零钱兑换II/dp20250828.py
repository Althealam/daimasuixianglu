# 1. dp数组以及下标的含义：dp[j]表示凑成总金额为j的总金额时，硬币组合数为dp[j]
# 2. 递推公式
# dp[j]+=dp[j-coin]
# 3. 初始化：全部初始化为0 dp[0]=1
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)
        dp[0] = 1
        for coin in coins:
            for j in range(1, amount+1):
                if j>=coin:
                    dp[j]+=dp[j-coin]
        return dp[amount]
        