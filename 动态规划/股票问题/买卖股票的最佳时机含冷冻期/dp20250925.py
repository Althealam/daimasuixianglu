# 1. dp数组以及下标的含义：
# 0表示第i天持有股票的状态下的最大利润，1表示第i天不持有股票状态下的最大利润，2表示第i天当前卖出股票状态下的最大利润，3表示第i天为冷冻期的状态下的最大利润
# 2. 递推公式
# dp[i][0] = max(dp[i-1][0], dp[i-1][1]-prices[i], dp[i-1][3]-prices[i])
# dp[i][1] = max(dp[i-1][1], dp[i-1][3])
# dp[i][2] = dp[i-1][0]+prices[i]
# dp[i][3] = dp[i-1][2]
# 3. 初始化：dp[i][0] = -prices[0]

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0]*4 for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]-prices[i], dp[i-1][3]-prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][3])
            dp[i][2] = dp[i-1][0]+prices[i]
            dp[i][3] = dp[i-1][2]
        return max(dp[-1][3], dp[-1][1], dp[-1][2])
        
        