# 1. dp数组以及下标的含义：dp[i][0]表示第i天不持有股票的最大收益，dp[i][1]表示第i天持有股票的最大收益
# 2. 递推公式：
# （1）dp[i][0]=max(dp[i-1][0], dp[i-1][1]+prices[i])
# （2）dp[i][1]=max(dp[i-1][1], -prices[i])
# 3. 初始化：dp[0][0]=0 dp[0][1]=-prices[0]
# 4. 遍历顺序：从前向后遍历
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp=[[0]*2 for _ in range(len(prices))]
        dp[0][1]=-prices[0]
        for i in range(1, len(prices)):
            dp[i][0]=max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1]=max(dp[i-1][1], -prices[i])
        return dp[-1][0]

        
        