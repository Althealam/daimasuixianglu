# 1. dp数组的含义：数组中某一天有两个状态，一个是买入，一个是卖出，因此我们需要定义一个二维数组
# dp[i][0]：持有股票的最大现金；dp[i][1]：不持有股票的最大现金（并不一定是当天买入或者卖出）
# 最终的结果：max(dp[len(prices)-1][0],dp[len(prices)-1][1])
# 2. 递推公式：
# dp[i][0]=max(dp[i-1][0],-prices[i])
# dp[i][1]=max(dp[i-1][1],dp[i-1][0]+prices[i])
# 3. 初始化
# dp[i]都是由dp[i-1]来的，并且需要dp[0][0]与dp[0][1]
# dp[0][0]=-prices[0];dp[0][1]=0
# 4. 遍历顺序
# 后面的状态依赖于前面的状态，因此是从前往后的遍历顺序

# 时间复杂度：for循环，O(n)
# 空间复杂度：dp数组大小为lengthx2，因此空间复杂度为O(n)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length=len(prices)
        if length==0:
            return 0
        dp=[[0]*2 for _ in range(length)]
        dp[0][0]=-prices[0]
        dp[0][1]=0
        for i in range(1,length):
            dp[i][0]=max(dp[i-1][0],-prices[i])
            dp[i][1]=max(dp[i-1][1],prices[i]+dp[i-1][0])
        return max(dp[length-1][0],dp[length-1][1])

solution=Solution()
prices=[7,1,5,3,6,4]
print(solution.maxProfit(prices))