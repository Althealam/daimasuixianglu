# 1. dp数组以及下标的含义：和为j的时候完全平方数的最少数量为dp[j]
# 2. 递推公式：
# （1）不考虑i：dp[j]
# （2）考虑i：dp[j-i**2]+1
# dp[j]=min(dp[j], dp[j-i**2]+1)
# 3. 初始化：求最少数量，因此全部初始化为正无穷 dp[0]=0
# 4. 遍历顺序：本题是求组合数，因此是先物品后背包
class Solution:
    def numSquares(self, n: int) -> int:
        dp=[float('inf')]*(n+1)
        dp[0]=0 
        for i in range(1, n+1):  # 遍历物品
            for j in range(i*i, n+1): # 遍历背包（需要确保背包剩下的容量是大于i*i的，否则j-i**2<0会出现报错）
                dp[j]=min(dp[j], dp[j-i**2]+1)
        return dp[n] 