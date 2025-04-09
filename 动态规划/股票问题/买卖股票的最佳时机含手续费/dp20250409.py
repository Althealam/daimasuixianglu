# 1. dp数组以及下标的含义：dp[i][0]表示保持今天持有股票的状态；dp[i][1]表示保持今天卖出股票的状态
# 2. 递推公式：
# （1）dp[i][0]=max(dp[i-1][0], dp[i-1][1]-prices[i]-fee)
# （2）dp[i][1]=max(dp[i-1][1], dp[i-1][0]+prices[i])
# 3. 初始化：dp[0][0]=-prices[0]-fee dp[0][1]=0
# 4. 遍历顺序：从前向后遍历
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp=[[0]*2 for _ in range(len(prices))]
        dp[0][0]=-prices[0]-fee
        for i in range(1, len(prices)):
            dp[i][0]=max(dp[i-1][0], dp[i-1][1]-prices[i]-fee)
            dp[i][1]=max(dp[i-1][1], dp[i-1][0]+prices[i])
        return dp[-1][1]
            
        