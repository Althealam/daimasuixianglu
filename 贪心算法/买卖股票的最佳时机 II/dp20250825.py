# 1. dp数组以及下标的含义：dp[i][0]表示在第i天买入股票的最大利润，dp[i][1]表示在第i天卖出股票的最大利润
# 2. 递推公式：
# dp[i][0] = max(dp[i-1][0], dp[i-1][1]-prices[i])
# dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[i])
# 3. 初始化：全部初始化为0 dp[i][0] = -prices[0]

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0]*2 for _ in range(len(prices))]
        for i in range(len(prices)):
            dp[i][0] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]-prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[i])
        return dp[-1][1]