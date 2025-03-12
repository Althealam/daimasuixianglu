# 1. dp数组以及下标的含义：dp[i][j]表示在第i天，状态为j的时候的最大收益是dp[i][j]
# 由上题可以知道：0是不持有，1是持有，2是不持有，因此奇数是持有，偶数是不持有
# 需要买卖k次，因此有2k+1种状态（0是不管的状态，我们最后要求解的是dp[-1][2*k]）
# 2. 递推公式：dp[i][0]=dp[i-1][0] 
# （1）j是奇数：dp[i][j]=max(dp[i-1][j], dp[i-1][j-1]+prices[i])
# （2）j是偶数：dp[i][j]=max(dp[i-1][j], dp[i-1][j-1]-prices[i])
# 3. 初始化：dp[0][0]=0 dp[0][1]=-prices[0] dp[0][2]=0 
# 当为奇数的时候 dp[0][j]=-prices[0] 当为偶数的时候dp[0][j]=0
# 4. 遍历顺序：从前向后遍历

# 时间复杂度：O(nk)
# 空间复杂度：O(nk)
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        dp=[[0]*(2*k+1) for _ in range(len(prices))]
        for j in range(1, 2*k+1):
            if j%2!=0:
                dp[0][j]=-prices[0]
            if j%2==0:
                dp[0][j]=0
        
        for i in range(1, len(prices)):
            for j in range(1, 2*k+1):
                if j%2!=0:
                    dp[i][j]=max(dp[i-1][j], dp[i-1][j-1]-prices[i])
                elif j%2==0:
                    dp[i][j]=max(dp[i-1][j], dp[i-1][j-1]+prices[i])
        
        return dp[-1][2*k]
        