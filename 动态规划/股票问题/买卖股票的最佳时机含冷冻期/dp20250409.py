# 1. dp数组以及下标的含义：
# （1）dp[i][0]表示第i天达到持有股票的状态时，最大利润为dp[i][0]
# （2）dp[i][1]表示第i天达到保持卖出股票的状态时，最大利润为dp[i][1]
# （3）dp[i][2]表示第i天达到今天卖出股票的状态时，最大利润为dp[i][2]
# （4）dp[i][3]表示第i天达到冷冻期的状态时，最大利润为dp[i][4]
# 2. 递推公式
# （1）dp[i][0]=max(dp[i-1][0],dp[i-1][3]-prices[i], dp[i-1][1]-prices[i])
# 之前就是买入股票的状态：dp[i-1][0]
# 昨天是冷冻期，今天买入股票：dp[i-1][3]-prices[i]
# 昨天不是冷冻期，今天买入股票：dp[i-1][1]-prices[i]
# （2）dp[i][1]=max(dp[i-1][1], dp[i-1][3])
# 前一天就是卖出股票的状态：dp[i-1][1]
# 保持卖出股票的状态，处于冷冻器：dp[i-1][3]
# （3）dp[i][2]=dp[i-1][0]+prices[i]
# 昨天持有股票，今天卖出股票 dp[i-1][0]+prices[i]
# （4）dp[i][3]=dp[i-1][2]
# 昨天卖出股票，今天是冷冻器
# 3. 初始化：dp[0][0]=-prices[0], dp[0][1]=0, dp[0][2]=0 dp[0][3]=0
# 4. 遍历顺序：从前向后遍历
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp=[[0]*4 for _ in range(len(prices))]
        dp[0][0]=-prices[0]
        for i in range(1, len(prices)):
            dp[i][0]=max(dp[i-1][0],dp[i-1][3]-prices[i],  dp[i-1][1]-prices[i])
            dp[i][1]=max(dp[i-1][1], dp[i-1][3])
            dp[i][2]=dp[i-1][0]+prices[i]
            dp[i][3]=dp[i-1][2]
        return max(dp[-1][1], dp[-1][2], dp[-1][3])

        