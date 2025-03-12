# 1. dp数组以及下标的含义：dp[i][j]中i表示第i天，j为0-4的五种状态，dp[i][j]表示第i天第j种状态的最大现金
# （0）没有操作（1）第一次持有股票（2）第一次不持有股票（3）第二次持有股票（4）第二次不持有股票
# 2. 递推公式：
# （1）dp[i][1]=max(dp[i-1][0]-prices[i], dp[i-1][1]) 
# 第一次第i天买入股票：dp[i-1][0]-prices[i] 第一次第i天没有买入股票（沿用买入股票的状态）：dp[i-1][1]
# （2）dp[i][2]=max(dp[i-1][1]+prices[i], dp[i-1][2])
# 第一次第i天卖出股票：dp[i-1][1]+prices[i] 第一次第i天没有卖出股票（沿用不持有股票的状态）：dp[i-1][2]
# （3）dp[i][3]=max(dp[i-1][2]-prices[i], dp[i-1][3])
# （4）dp[i][4]=max(dp[i-1][3]+prices[i], dp[i-1][4])
# 3. 初始化：dp[0][0]=0 dp[0][1]=-prices[0] dp[0][2]=0 dp[0][3]=-prices[0] dp[0][4]=0
# 4. 遍历顺序：从前向后遍历

# 时间复杂度：O(n)
# 空间复杂度：O(n)

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp=[[0]*5 for _ in range(len(prices))]
        dp[0][0]=0
        dp[0][1]=-prices[0]
        dp[0][2]=0
        dp[0][3]=-prices[0]
        dp[0][4]=0

        for i in range(1, len(prices)):
            dp[i][0]=dp[i-1][0]
            dp[i][1]=max(dp[i-1][0]-prices[i], dp[i-1][1])
            dp[i][2]=max(dp[i-1][1]+prices[i], dp[i-1][2])
            dp[i][3]=max(dp[i-1][2]-prices[i], dp[i-1][3])
            dp[i][4]=max(dp[i-1][3]+prices[i], dp[i-1][4])
        
        return dp[len(prices)-1][4]
            
        