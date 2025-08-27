# 1. dp数组以及下标的含义：dp[i][j]表示从[0,0]到[i,j]有dp[i][j]条路径
# 2. 递推公式：
# dp[i][j] = dp[i-1][j]+dp[i][j-1]
# 3. 初始化：全部初始化为0 dp[i][0] = 1 dp[0][j] = 1
# 4. 遍历顺序：从左到右，从上到下
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]