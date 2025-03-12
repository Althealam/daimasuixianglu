# 方法：动态规划
# 1. dp数组的含义：
# （1）dp[i][0]表示第i天持有股票所得现金
#       第i-1天持有股票，那么就保持现状，所得现金就是昨天持有股票的所得现金，即dp[i-1][0]
#       第i天买入股票，所得现金就是昨天不持有股票的所得现金减去今天的股票价格，即dp[i-1][1]-prices[i]（这个和买卖一次的状况不同）
# （2）dp[i][1]表示第i天不持有股票所得的最多现金
#       第i-1天就不持有股票，那么就保持现状，所得现金就是昨天不持有股票的所得现金 即：dp[i - 1][1]
#       第i天卖出股票，所得现金就是按照今天股票价格卖出后所得现金即：prices[i] + dp[i-1][0] 

# 时间复杂度：O(n)
# 空间复杂度：O(n)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length=len(prices)
        dp=[[0]*2 for _ in range(length)]
        dp[0][0]=-prices[0]
        dp[0][1]=0

        for i in range(1,length):
            dp[i][0]=max(dp[i-1][0],dp[i-1][1]-prices[i])
            dp[i][1]=max(dp[i-1][1],prices[i]+dp[i-1][0])
        
        return max(dp[length-1][0],dp[length-1][1])

