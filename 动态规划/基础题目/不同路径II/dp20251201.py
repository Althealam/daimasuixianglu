# 1. the definition of dp: dp[i][j] denotes the number of paths which make robot moves to [i, j]
# 2. formula: dp[i][j] = dp[i-1][j]+dp[i][j-1]
# 3. initialize: dp[i][0] = 1 dp[0][j] = 1
# if obstacleGrid[i][0]==1: dp[i][0] = 0 break 
# if obstacleGrid[0][j]==1: dp[0][j] = 0 break
# if obstacleGrid[0][0]==1 of obstacleGrid[-1][-1]==1: return 0
# 4. order: left-right top-bottom
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0]==1 or obstacleGrid[-1][-1]==1:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0]==1:
                dp[i][0] = 0
                break
            else:
                dp[i][0]=1
        for j in range(n):
            if obstacleGrid[0][j]==1:
                dp[0][j] = 0
                break
            else:
                dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j]!=1:
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]