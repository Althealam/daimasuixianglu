# 1. definition: dp[i][0] means the maximal profit I can achieve in one day while you have stock, and dp[i][1] means the maximal profit I can achieve in one day while I don't have stock
# 2. formula:
# dp[i][0] = max(dp[i-1][1]-prices[i], dp[i-1][0])
# dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[i])
# 3. initialization: dp=[[0]*2 for _ in range(len(prices))]
# dp[0][0]=-prices[0] dp[0][1]=0
# 4. order: left to right
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0]*2 for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][1]-prices[i], dp[i-1][0])
            dp[i][1] = max(dp[i-1][0]+prices[i], dp[i-1][1])
        return dp[-1][1]

        