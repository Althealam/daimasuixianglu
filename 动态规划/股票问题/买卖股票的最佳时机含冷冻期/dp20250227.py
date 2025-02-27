# 1. dp数组以及下标的含义：dp[i][j]表示第i天的时候状态为j，所剩下的最多现金为dp[i][j]
# ## （1）保持买入股票的状态 dp[i][0]
# （1.1）前一天就是持有股票的状态：dp[i-1][0]
# （1.2）今天买入了股票：（1）前一天是冷冻期：dp[i-1][3]-prices[i] （2）前一天不是冷冻期：dp[i-1][1]-prices[i]
# ## （2）保持卖出股票的状态 dp[i][1]
# （2.1）前一天就是卖出股票的状态：dp[i-1][1]
# （2.2）前一天是冷冻期：dp[i-1][3]
# ## （3）今天卖出股票的状态 dp[i][2]
# （3.1）昨天持有股票并且今天卖出：dp[i-1][0]+prices[i]
# ## （4）达到冷冻期状态 dp[i][3]
# （4.1）达到冷冻期也就是昨天卖出了股票：dp[i-1][2]
# 2. 递推公式
# dp[i][0]=max(dp[i-1][0], dp[i-1][3]-prices[i], dp[i-1][1]-prices[i])
# dp[i][1]=max(dp[i-1][1], dp[i-1][3])
# dp[i][2]=dp[i-1][0]+prices[i]
# dp[i][3]=dp[i-1][2]
# 3. 初始化：dp[0][0]=-prices[0] dp[0][1]=0 dp[0][2]=0 dp[0][3]=0
# 4. 遍历顺序：从前向后遍历

# 时间复杂度：O(n)
# 空间复杂度：O(n)

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==0:
            return 0
        dp=[[0]*4 for _ in range(len(prices))]
        dp[0][0]=-prices[0]

        for i in range(1, len(prices)):
            dp[i][0]=max(dp[i-1][0], dp[i-1][3]-prices[i], dp[i-1][1]-prices[i])
            dp[i][1]=max(dp[i-1][1], dp[i-1][3])
            dp[i][2]=dp[i-1][0]+prices[i]
            dp[i][3]=dp[i-1][2]
        
        return max(dp[len(prices)-1][3], dp[len(prices)-1][1], dp[len(prices)-1][2])

        