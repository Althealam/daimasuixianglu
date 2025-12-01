# 1. the definition of dp: dp[i][j] denotes the number of paths which can make robot move to [i, j] in the matrix
# 2. recurrence formula: dp[i][j] = dp[i-1][j]+dp[i][j-1]
# 3. initialize: dp[0][0] = 1 dp[i][0] = 1 dp[0][j] = 1
# 4. travesal order: left-right top-bottom
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
        
        
        