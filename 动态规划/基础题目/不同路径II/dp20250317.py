# 1. dp数组以及下标的含义：dp[i][j]表示到达[i,j]有dp[i][j]条路径
# 2. 递推公式：dp[i][j]=dp[i-1][j]+dp[i][j-1] 遇到障碍物时则直接跳过
# 3. 初始化：dp[i][0]=1 dp[0][j]=1
# 如果obstacleGrid[i][0]=1，那么该位置后面的i都为0；同理如果obstacleGrid[0][j]为1，那么该位置后面的j都为0
# 4. 遍历顺序：从左到右，从上到下

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n=len(obstacleGrid), len(obstacleGrid[0])
        dp=[[0]*m for _ in range(n)]
        for i in range(m):
            if obstacleGrid[i][0]==0:
                dp[i][0]=1
            else: # 遇到障碍物时直接退出循环
                break
        for j in range(n):
            if obstacleGrid[0][j]==0:
                dp[0][j]=1
            else: # 遇到障碍物时直接退出循环
                break
        for i in range(1,m):
            for j in range(1, n):
                if obstacleGrid[i][j]==1: # 遇到障碍物，则跳过
                    continue
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]
        