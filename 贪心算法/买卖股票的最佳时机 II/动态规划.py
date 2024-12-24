# 方法：动态规划
# 时间复杂度：从索引1到length-1的for循环
# 总的时间复杂度为O(n)
# 空间复杂度：使用了一个二维数组dp，其大小为length*2
# 总的空间复杂度为O(n)
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
            dp[i][1]=max(dp[i-1][1],dp[i-1][0]+prices[i])
        return dp[-1][1]
        