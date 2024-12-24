# 分析：
# 1. dp数组的含义：
# dp[i][0]持有股票的状态
# dp[i][1]保持卖出股票的状态；
# dp[i][2]指的是卖出股票的状态（由于题目有冷冻期，因此需要讨论卖出股票和冷冻期的两个状态）
# dp[i][3]指的是冷冻期（持续一天，并且冷冻期的前一天一定是卖出股票的状态）
# 2. 递推公式
# dp[i][0]=max(dp[i-1][0],dp[i-1][1]-prices[i],dp[i-1][3]-prices[i])（分别是保持状态，以及第i天买入股票，以及前一天是冷冻期后买入股票）
# dp[i][1]=max(dp[i-1][1],dp[i-1][3])
# dp[i][2]=dp[i-1][0]+prices[i]
# dp[i][3]=dp[i-1][2]
# 3. 初始化
# dp[0][0]=-prices[0];dp[0][1]=0（非法状态，从递推公式解释）;dp[0][2]=0;dp[0][3]=0
# 4. 遍历顺序

# 时间复杂度：
# 1. 外层循环：遍历prices数组，长度为n
# 2. 状态转移：O(1)
# 总的时间复杂度为O(n)
# 空间复杂度：
# dp表长度为nx4
# 总的空间复杂度为O(n)

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

        for i in range(1,len(prices)):
            dp[i][0]=max(dp[i-1][0],dp[i-1][1]-prices[i],dp[i-1][3]-prices[i])
            dp[i][1]=max(dp[i-1][1],dp[i-1][3])
            dp[i][2]=dp[i-1][0]+prices[i]
            dp[i][3]=dp[i-1][2]
        return max(dp[len(prices)-1][3],dp[len(prices)-1][2],dp[len(prices)-1][1])



        