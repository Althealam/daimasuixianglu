# 1. dp数组以及下标的含义：dp[i][0]表示第i天持有股票所得到的最多现金，dp[i][1]表示第i天不持有股票所得到的最多现金
# 2. 递推公式：
# dp[i][0]=max(dp[i-1][0], dp[i-1][1]-prices[i])
# dp[i][1]=max(dp[i-1][1], dp[i-1][0]+prices[i]-fee)
# 3. 初始化：dp[0][0]=-prices[0] dp[0][1]=0
# 4. 遍历顺序：从前向后

# 时间复杂度：O(n)
# 空间复杂度：O(n)

class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        dp=[[0]*2 for _ in range(len(prices))]
        dp[0][0]=-prices[0]
        for i in range(1, len(prices)):
            dp[i][0]=max(dp[i-1][0], dp[i-1][1]-prices[i])
            dp[i][1]=max(dp[i-1][1], dp[i-1][0]+prices[i]-fee)
        return dp[-1][1]
        