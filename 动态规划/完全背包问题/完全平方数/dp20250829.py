# 1. dp数组以及下标的含义：dp[j]表示和为j的完全平方数的最少数量
# 2. 递推公式：
# dp[j] = min(dp[j], dp[j-i**2]+1)
# 3. 初始化：全部初始化为float('inf') dp[0] = 0

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        for j in range(1, n+1):
            for i in range(1, j):
                if j>=i*i:
                    dp[j] = min(dp[j], dp[j-i*i]+1)
        return dp[-1] if dp[-1]!=float('inf') else -1
        