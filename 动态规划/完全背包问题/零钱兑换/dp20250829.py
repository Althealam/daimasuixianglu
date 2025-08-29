# 1. dp数组以及下标的含义：dp[j]表示填充金额为j的面额时所需要的最少硬币个数
# 2. 递推公式：
# dp[j] = min(dp[j], dp[j-coin]+1)
# 3. 初始化：全部初始化为float('inf') 并且dp[0] = 0
# 4. 遍历顺序：从前向后遍历
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for coin in coins:
            for j in range(1, amount+1):
                if j>=coin:
                    dp[j] = min(dp[j], dp[j-coin]+1)
        return dp[-1] if dp[-1]!=float('inf') else -1
        