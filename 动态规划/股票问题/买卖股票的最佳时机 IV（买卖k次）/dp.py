# 区别：最多可以完成k笔交易
# 1. dp数组：dp[i][j]：第i天的状态为j，所剩下的最大现金是dp[i][j]
# 0表示不操作；1表示第一次买入；2表示第一次卖出；3表示第二次买入；4表示第二次卖出
# 总结：奇数表示买入，偶数表示卖出
# 2. 递推公式：
# （1）dp[i][1]：
#               第i天买入股票：dp[i][1]=dp[i-1][0]-prices[i]
#               第i天没有操作：dp[i][1]=dp[i-1][1]
# dp[i][1]=max(dp[i-1][0]-prices[i],dp[i-1][1])
# （2）dp[i][2]：
#               第i天卖出股票：dp[i][2]=dp[i-1][1]+prices[i]
#               第i天没有操作：dp[i][2]=dp[i-1][2]
# dp[i][2]=max(dp[i-1][1]+prices[i],dp[i-1][2])
# 3. dp数组的初始化：
# dp[0][0]=0;dp[0][1]=-prices[0];dp[0][2]=0;dp[0][3]=-prices[0];dp[0][4]=0
# dp[0][j]：当j为奇数的时候，则为-prices[0]；当j为偶数的时候，则为0
# 由于可以最多买卖k次，因此数组的长度至少为2*k+1
# 参考上一题，最多可以买卖两次，因此数组的长度为5，也就是dp[i][0],...,dp[i][5]
# 4. 遍历顺序：从前向后遍历

# 时间复杂度：
# 1. 外层循环执行了n次；
# 2. 内层循环遍历2k个交易状态中的每一对
# 总的时间复杂度为O(n*k)
# 空间复杂度：
# 1. dp表，大小为nx(2k+1)
# 总的空间复杂度为O(n*k)

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==0:
            return 0
        length=len(prices)
        dp=[[0]*(2*k+1) for _ in range(length)]
        # 初始化奇数下标的dp为-prices[0]
        for j in range(1,2*k,2):
            dp[0][j]=-prices[0]
        # 计算状态转移方程
        for i in range(1,len(prices)):
            for j in range(0,2*k-1,2):
                dp[i][j+1]=max(dp[i-1][j+1],dp[i-1][j]-prices[i])
                dp[i][j+2]=max(dp[i-1][j+2],dp[i-1][j+1]+prices[i])
        return dp[length-1][2*k]
        