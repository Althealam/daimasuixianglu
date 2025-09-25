# 1. dp数组以及下标的含义：dp[i][0]表示在第i天第一次持有股票的最大收益，dp[i][1]表示在第i天第一次不持有股票的最大收益，dp[i][2]表示在第i天第二次持有股票的最大收益，dp[i][3]表示在第i天第二次不持有股票的最大收益
# 2. 递推公式
# dp[i][0] = max(dp[i-1][0], -prices[0])
# dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[i])
# dp[i][2] = max(dp[i-1][2], dp[i-1][1]-prices[i])
# dp[i][3] = max(dp[i-1][3], dp[i-1][2]+prices[i])
# 3. 初始化：dp[0][0]=dp[0][2] = -prices[0]

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0]*4 for _ in range(len(prices))]
        dp[0][0], dp[0][2] = -prices[0], -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], -prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[i])
            dp[i][2] = max(dp[i-1][2], dp[i-1][1]-prices[i])
            dp[i][3] = max(dp[i-1][3], dp[i-1][2]+prices[i])
        return dp[-1][3]        