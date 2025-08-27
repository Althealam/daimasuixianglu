# 1. dp数组以及下标的含义：dp[i][j]表示从[0, 0]到[i, j]的不同路径数量
# 2. 递推公式：
# if grid[i][j]==0: dp[i][j] = 0
# else: dp[i][j] = dp[i-1][j]+dp[i][j-1]
# 3. 初始化：全部初始化为0 遍历[i,0]和[0,j] 如果遇到障碍则跳过
# 4. 遍历顺序：从左到右 从上到下
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[0]*len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        for i in range(len(obstacleGrid)):
            if obstacleGrid[i][0]==1:
                break
            else:
                dp[i][0]=1
        for j in range(len(obstacleGrid[0])):
            if obstacleGrid[0][j]==1:
                break
            else:
                dp[0][j]=1
        
        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                if obstacleGrid[i][j]==1:
                    continue
                else:
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]
        