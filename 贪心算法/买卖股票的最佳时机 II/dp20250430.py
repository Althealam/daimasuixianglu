# 1. dp数组以及下标的含义：dp[i][0]表示第i天持有股票的最大收益，dp[i][1]表示在第i天不持有股票的最大收益
# 2. 递推公式：
# dp[i][0]：
# （1）第i-1天持有股票：dp[i-1][0]
# （2）第i-1天不持有股票：dp[i-1][1]-prices[i]
# dp[i][1]
# （1）第i-1天不持有股票：dp[i-1][1]
# （2）第i-1天持有股票：dp[i-1][0]+prices[i]
# 3. 初始化：dp[0][0]=-prices[0]
# 4. 遍历顺序：从左到右


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp=[[0]*2 for _ in range(len(prices))]
        dp[0][0]=-prices[0]
        dp[0][1]=0
        for i in range(1, len(prices)):
            dp[i][0]=max(dp[i-1][0], dp[i-1][1]-prices[i])
            dp[i][1]=max(dp[i-1][1], dp[i-1][0]+prices[i])
        
        return max(dp[-1][0], dp[-1][1])