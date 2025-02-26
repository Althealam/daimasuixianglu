# 1. dp数组以及下标的含义：dp[j]表示和为j的完全平方数的最少数量为dp[j]
# 2. 递推公式：dp[j]=min(dp[j], dp[j-i*i]+1)
# （1）不考虑i：dp[j]
# （2）考虑i：dp[j-i*i]+1
# 3. 初始化：dp初始化为无穷大 dp[0]=0
# 4. 遍历顺序：先物品后背包，先背包后物品

# 这里的物品值为x*x<=n: x<=n**(0.5)，因此物品值的上限是int(n**(0.5))

# 时间复杂度：O(n**(3/2))
# 1. 外层循环：O(n**0.5)
# 2. 内层循环：O(n)
# 空间复杂度：O(n)
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[float('inf')]*(n+1)
        dp[0]=0

        for i in range(1,int(n**(0.5))+1): # 遍历物品
            for j in range(i*i, n+1): # 遍历背包
                dp[j]=min(dp[j], dp[j-i*i]+1)
        return dp[n]
        