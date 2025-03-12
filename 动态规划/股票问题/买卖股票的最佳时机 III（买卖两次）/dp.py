# 动态规划五部曲
# 1. dp数组的含义：dp[i][0]定义为不操作；dp[i][1]定义为第一次持有（可能是延续前一天持有的状态，不一定是第i天买入）；dp[i][2]定义为第一次不持有；dp[i][3]定义为第二次持有；dp[i][4]定义为第二次不持有
# 2. 递推公式：dp[i][0]=dp[i-1][0]
# dp[i][1]= max(dp[i-1][1],dp[i-1][0]-prices[i])(dp[i-1][0]-prices[i]表示的是今天买入，前几天没买入)
# dp[i][2]=max(dp[i-1][2],dp[i-1][1]+prices[i])(dp[i-1][1]+prices[i]表示的是前一天持有，今天卖出)
# dp[i][3]=max(dp[i-1][3],dp[i-1][2]-prices[i])
# dp[i][4]=max(dp[i-1][4],dp[i-1][3]+prices[i])
# 3. 初始化：
# dp[0][0]=0; dp[0][1]=-prices[0];dp[i][3]=-prices[0];dp[i][4]=0

# 时间复杂度：
# 1. 外层循环遍历prices数组，长度为n，因此外层循环执行了n-1次
# 内层操作涉及dp[i][1]到dp[i][4]的状态转移计算
# 总的时间复杂度为O(n)

# 空间复杂度：
# 1. 使用了二维数组dp，大小为nx5
# 总的空间复杂度为O(n)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length=len(prices)
        dp=[[0]*5 for _ in range(length)]
        dp[0][1]=-prices[0]
        dp[0][3]=-prices[0]

        for i in range(1,length):
            dp[i][1]=max(dp[i-1][1],dp[i-1][0]-prices[i])
            dp[i][2]=max(dp[i-1][2],dp[i-1][1]+prices[i])
            dp[i][3]=max(dp[i-1][3],dp[i-1][2]-prices[i])
            dp[i][4]=max(dp[i-1][4],dp[i-1][3]+prices[i])
        return dp[length-1][4]
        