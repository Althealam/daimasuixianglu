# 1. dp数组以及下标的含义：
# （1）dp[i][j]（j为偶数）表示第i天持有股票的最大收益
# （2）dp[i][j]（j为奇数）表示第i天不持有股票的最大收益
# 2. 递推公式
# dp[i][0]=max(dp[i-1][0], -prices[i])
# dp[i][j]=max(dp[i-1][j], dp[i-1][j-1]-prices[i])（j为偶数）
# dp[i][j]=max(dp[i-1][j], dp[i-1][j-1]+prices[i])（j为奇数）
# 3. 初始化：dp[0][0]=-prices[0] dp[0][j]=-prices[0]（j为奇数）
# 4. 遍历顺序：从左到右，从上到下

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp=[[0]*2*k for _ in range(len(prices))]
        for j in range(2*k):
            if j%2==0:
                dp[0][j]=-prices[0] 
        for i in range(1, len(prices)):
            for j in range(2*k):
                if j==0:
                    dp[i][0]=max(dp[i-1][0], -prices[i])
                elif j%2==0:
                    dp[i][j]=max(dp[i-1][j], dp[i-1][j-1]-prices[i])
                else:
                    dp[i][j]=max(dp[i-1][j], dp[i-1][j-1]+prices[i])
        return dp[-1][-1]
