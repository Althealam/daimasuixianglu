# 1. dp数组以及下标的含义：dp[i][j]表示移动到[i, j]时的路径总数
# 2. 递推公式
# dp[i][j] = dp[i-1][j]+dp[i][j-1]
# 3. 初始化：dp[i][0] = 1 dp[0][j]=1 
# 如果遇到了obstacleGrid[i][j]==1 那么其该行和该列后面都为0
# 4. 遍历顺序：从上到下 从左到右
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0]==1 or obstacleGrid[-1][-1]==1:
            return 0
        dp = [[0]*len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        for i in range(len(obstacleGrid)):
            if obstacleGrid[i][0]==1:
                break
            dp[i][0] = 1
        for j in range(len(obstacleGrid[0])):
            if obstacleGrid[0][j]==1:
                break
            dp[0][j]=1
        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                if obstacleGrid[i][j]==0:
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]
        